# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        title = item['title']
        movie_type = item['movie_type']
        movie_date = item['movie_date']
        output = f'{title},{movie_type},{movie_date}\n'
        with open('./maoyan_xpath.csv','a+',encoding='utf-8') as article:
            article.write(output)
        return item
