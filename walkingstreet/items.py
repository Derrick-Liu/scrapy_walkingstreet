# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PersonalInfoItem(scrapy.Item):
	'''用户个人信息'''
    # define the fields for your item here like:
    # name = scrapy.Field()
	nickname=scrapy.Field()
	gender=scrapy.Field()
	location=scrapy.Field()
	level=scrapy.Field()
	association=scrapy.Field()
	money_remain=scrapy.Field()
	online_time=scrapy.Field()
	register_time=scrapy.Field()
	last_login=scrapy.Field()
	self_introduce=scrapy.Field()
	image_url=scrapy.Field()
	favorate_sports=scrapy.Field()
	favorate_association=scrapy.Field()
	favorate_teams=scrapy.Field()
	
	following_count=scrapy.Field()
	fans_count=scrapy.Field()
	
	
	
class FollowItem(scrapy.Item):
	'''用户关注信息'''
	following=scrapy.Field()
	followed=scrapy.Field()

class FollowCountItem(scrapy.Item):
	'''用户关注数量信息'''
	nickname=scrapy.Field()
	following_count=scrapy.Field()
	fans_count=scrapy.Field()
	
