# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'anlei6666',
    'db' : 'test'
}

class ZdmtopPipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db'])
        cur = conn.cursor()

        try:
            title = item['title']
            comments = item['comments']
            for comment in comments:
                sql = 'insert into zdm_comment(title,comment,comment_date) values (%s,%s,%s)'
                cur.execute(sql,(title,comment['commentText'],comment['commentDate']))
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        
        conn.close()
        return item