#coding:utf-8
from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from walkingstreet.items import PersonalInfoItem,FollowItem,FollowCountItem
from scrapy.selector import Selector
from walkingstreet.settings import COOKIES
#from scrapy import log
import pymysql

import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class WalkingStreet(CrawlSpider):
	
	name='profile'
	start_url='https://my.hupu.com/er_yuan_hua_shi'
	url_to_crawl=[]
	url_crawled={}
	
	def start_requests(self):    #该方法的默认实现是使用 start_urls 的url生成Request
		return[Request(
		url=self.start_url+'/profile',
		cookies=COOKIES,
		meta={'URL':self.start_url},
		callback=self.parse_info)
		]
		
	def parse_info(self,response):
		item=PersonalInfoItem()
		selector=Selector(response)

		item['nickname']=selector.xpath('//*[@id="headtop"]/h1/text()').extract_first(default='unknown')[:-3]
		item['image_url'] = selector.xpath('//*[@id="headtop"]/a/img/@src').extract_first(default='unknown')
		item['gender']=selector.xpath('//*[@id="content"]/table[1]/tr[1]/td[2]/text()').extract_first(default='unknown')

		second=selector.xpath('//*[@id="content"]/table[1]/tr[2]/td[1]/text()').extract_first(default='unknown')
		if second==u'所在地：':
			item['location']=selector.xpath('//*[@id="content"]/table[1]/tr[2]/td[2]/text()').extract_first(default='unknown')
			i=3
		else:
			item['location']='unknown'
			i=2
		item['level']=selector.xpath('//*[@id="content"]/table[1]/tr[%d]/td[2]/text()'%i).extract_first(default='unknown')
		item['association']=selector.xpath('//*[@id="content"]/table[1]/tr[%d]/td[2]/text()'%(i+1)).extract_first(default='unknown')
		item['money_remain']=selector.xpath('//*[@id="content"]/table[1]/tr[%d]/td[2]/text()'%(i+2)).extract_first(default='unknown')
		item['online_time']=selector.xpath('//*[@id="content"]/table[1]/tr[%d]/td[2]/text()'%(i+3)).extract_first(default='unknown')
		item['register_time']=selector.xpath('//*[@id="content"]/table[1]/tr[%d]/td[2]/text()'%(i+4)).extract_first(default='unknown')
		item['last_login']=selector.xpath('//*[@id="content"]/table[1]/tr[%d]/td[2]/text()'%(i+5)).extract_first(default='unknown')
		intro=selector.xpath('//*[@id="content"]/table[1]/tr[%d]/td[2]'%(i+6))
		info=''.join(intro.xpath('string(.)').extract())
		item['self_introduce']=info

		item['favorate_sports']=selector.xpath('//*[@id="content"]/table[2]/tr[1]/td[2]/text()').extract_first(default='unknown')
		item['favorate_association']=selector.xpath('//*[@id="content"]/table[2]/tr[2]/td[2]/text()').extract_first(default='unknown')
		item['favorate_teams']=selector.xpath('//*[@id="content"]/table[2]/tr[3]/td[2]/text()').extract_first(default='unknown')

		url_following=response.meta["URL"]+'/following'
		url_follower=response.meta["URL"]+'/follower'
		yield Request(url=url_following,meta={"nickname":item.get('nickname')},callback=self.get_following,errback=self.parse_err)
		yield Request(url=url_follower,meta={"nickname":item.get('nickname')},callback=self.get_fans,errback=self.parse_err)
		
		yield item
		
		
	
	def get_following(self,response):

		selector=Selector(response)
		current_name=response.meta["nickname"]
		

		
		#爬取关注页面第一页时，将关注人数和粉丝人数输出item
		if not response.meta.get("page_next"):
			following_num=selector.xpath('//*[@id="content"]/div[2]/div[1]/ul/li[1]/a/span/text()').re_first(r'\((.*?)\)')
			fans_num=selector.xpath('//*[@id="content"]/div[2]/div[1]/ul/li[2]/a/span/text()').re_first(r'\((.*?)\)')
			item = FollowCountItem()
			item['nickname']=current_name
			item['following_count']=following_num
			item['fans_count']=fans_num
			yield item


		nickname_list = selector.xpath('//*[@id="content"]/div[2]/div[2]/ul/li/div/div[1]/strong/a/text()').extract()
		url_list=selector.xpath('//*[@id="content"]/div[2]/div[2]/ul/li/div/div[1]/strong/a/@href').extract()
		for i in range(len(url_list)):
			if not self.url_crawled.has_key(url_list[i]):
				# 关注列表，当前用户是关注人，列表中是被关注人
				# 防止关注列表有重复，同样已检索过的用户不再产生关注关系
				# 对下面get_fans()函数做同样的修改
				item = FollowItem()
				item['following'] = current_name
				item['followed'] = nickname_list[i]
				yield item

				self.url_crawled[url_list[i]]=1
				yield Request(
				url=url_list[i]+'/profile',
				cookies=COOKIES,
				meta={'URL':url_list[i]},
				callback=self.parse_info
				)
				
		
		page_next=selector.xpath('//*[@id="content"]/div[2]/div[3]/span/a[@class="next"]/@href').extract_first()
		if page_next:
			complete_url='https://my.hupu.com'+page_next
			yield Request(
			url=complete_url,
			callback=self.get_following,
			meta={"nickname":current_name,"page_next":1},
			cookies=COOKIES,
			errback=self.parse_err)
			
			

	def get_fans(self,response):

		selector=Selector(response)
		current_name=response.meta["nickname"]

		nickname_list = selector.xpath('//*[@id="content"]/div[2]/div[2]/ul/li/div/div[1]/strong/a/text()').extract()
		url_list=selector.xpath('//*[@id="content"]/div[2]/div[2]/ul/li/div/div[1]/strong/a/@href').extract()
		for i in range(len(url_list)):
			if not self.url_crawled.has_key(url_list[i]):
				# 关注列表，当前用户是被关注人，列表中是关注人
				item = FollowItem()
				item['following'] = nickname_list[i]
				item['followed'] = current_name
				yield item

				self.url_crawled[url_list[i]]=1
				yield Request(
				url=url_list[i]+'/profile',
				meta={'URL':url_list[i]},
				cookies=COOKIES,
				callback=self.parse_info
				)
		
		
		page_next=selector.xpath('//*[@id="content"]/div[2]/div[3]/span/a[@class="next"]/@href').extract_first()
		if page_next:
			complete_url='https://my.hupu.com'+page_next
			yield Request(
			url=complete_url,
			cookies=COOKIES,
			callback=self.get_fans,
			meta={"nickname":current_name},
			errback=self.parse_err)
		
		
	def parse_err(self, response):
		#log.ERROR('crawl {} failed'.format(response.url))
		pass

	
