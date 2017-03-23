# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from walkingstreet.items import PersonalInfoItem,FollowItem,FollowCountItem
import pymysql
from datetime import datetime

class WalkingstreetPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='lshi6060660',
            db='walkingstreet',
            charset='utf8'
        )
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

        if isinstance(item,PersonalInfoItem):
            info=(item.get('nickname'),
                  item.get('gender'),
                  item.get('location'),
                  item.get('level'),
                  item.get('association'),
                  item.get('money_remain'),
                  item.get('online_time'),
                  item.get('register_time'),
                  item.get('last_login'),
                  item.get('self_introduce'),
                  item.get('image_url'),
                  item.get('favorate_sports'),
                  item.get('favorate_association'),
                  item.get('favorate_teams')
                  )
            Insert_info="INSERT profile (nickname,gender,location,level,association,money_remain,online_time," \
                        "register_time,last_login,self_introduce,image_url,favorate_sports,favorate_associations," \
                        "favorate_teams) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(Insert_info,info)

        if isinstance(item,FollowItem):
            follow=(item.get('following'),
                 item.get('followed'))
            Insert_Follow="INSERT followship VALUES (%s,%s)"
            cur.execute(Insert_Follow,follow)

        if isinstance(item,FollowCountItem):
            info=(item.get('nickname'),
                  item.get('following_count'),
                  item.get('fans_count')
                  )
            Count_info = "INSERT follow_count VALUES (%s,%s,%s)"
            cur.execute(Count_info,info)

        cur.close()
        conn.commit()
        conn.close()
        return item