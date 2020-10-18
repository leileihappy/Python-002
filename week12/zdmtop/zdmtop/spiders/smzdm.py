# -*- coding: utf-8 -*-
import scrapy
from zdmtop.items import ZdmtopItem
from scrapy.selector import Selector

class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1']

    def start_requests(self):
        url = f'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1'
        yield scrapy.Request(url=url,callback=self.parse,dont_filter=False)
    
    def parse(self, response):
        phones = Selector(response=response).xpath('//*[@id="feed-main-list"]/li/div/div[2]')
        for i in range(10):
            phone = phones[i]
            link = phone.xpath('./h5/a/@href').get()
            title=phone.xpath('./h5/a/text()').get()
            #print('aaaaaaab'+str(i)+','+str(link)+','+str(title))
            item=ZdmtopItem()
            item['title']=title
            perpage = 30
            size = int(phone.xpath('./div[4]/div[1]/a[2]/span/text()').get())
            pageSize = self.complexPage(size,perpage)
            for j in range(1,pageSize+1):
                if j == 1:
                    yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)
                else:
                    linknew = link + f'p{j}'+'/#comments'
                    print('linknew='+str(linknew))
                    yield scrapy.Request(url=linknew,meta={'item':item},callback=self.parse2)
    
    def parse2(self,response):
        item = response.meta['item']
        lists = Selector(response=response).xpath('//*[@id="commentTabBlockNew"]/ul[1]/li[@class="comment_list"]')
        comments = []
        for comment in lists:
            commentText = comment.xpath('./div[2]/div[2]/div[1]/p/span/text()').get()
            commentDate = comment.xpath('./div[2]/div[1]/div[1]/meta/@content').get()
            comments.append({'commentText':commentText,'commentDate':commentDate})
        item['comments'] = comments
        return item
    
    def complexPage(self,size,perpage):
        aa = size % perpage
        page=int(size/perpage)
        if aa>0:
            page=page+1
        return page




