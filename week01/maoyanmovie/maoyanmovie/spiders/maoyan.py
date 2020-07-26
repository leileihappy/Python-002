# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse,dont_filter=False)
    
    def parse(self,response):
        i = 0 
        items = []
        movies_list = Selector(response=response).xpath('//dl[@class="movie-list"]//dd')
        for movie in movies_list:
            if i >9:
                break
            item = MaoyanmovieItem()
            title = movie.xpath('./div/@title').get()
            movie_data = movie.xpath('./div[@class="movie-item film-channel"]/div/a/div/div/text()').extract()
            movie_list = [x.strip() for x in movie_data if x.strip() != '']
            movie_type = movie_list[0]
            movie_date = movie_list[2]
            item['title'] = title
            item['movie_type'] = movie_type
            item['movie_date'] = movie_date
            items.append(item)
            i = i+1
        return items

