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
    'password' : 'anlei666',
    'db' : 'test'
}


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'anlei666',
            db = 'test')
        cur = conn.cursor()

        try:
            title = item['title']
            movie_type = item['movie_type']
            movie_date = item['movie_date']
            sql = 'insert into maoyan_movie(title,movie_type,movie_date) values ("' + title + '","'+ movie_type+'","'+movie_date +'")'
            cur.execute(sql)
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        
        conn.close()

        # output = f'{title},{movie_type},{movie_date}\n'
        # with open('./maoyan_xpath.csv','a+',encoding='utf-8') as article:
        #     article.write(output)

        return item
