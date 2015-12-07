# -*- coding:utf-8 -*-
__author__ = 'prm14'
import scrapy
from scrapy import Selector
import logging

from web_crawling.items import WebCrawlingItem

class MobileSpider(scrapy.Spider):
    name="pconline"
    allowed_domains = ["product.pconline.com.cn/mobile/"]
    start_urls = [
        "http://mobile.pconline.com.cn/",
        "http://product.pconline.com.cn/mobile/"
    ]
    def parse(self, response):
        sel=Selector(response)
        sites=sel.xpath('//li[@class="item"]/div[@class="item-wrap"]')
        items=[]
        info=str(len(sites))+" mobile info have been found"
        logging.info(info.encode('utf-8'))
        for site in sites:
            item=WebCrawlingItem()

            site1=site.xpath('div[@class="item-detail"]/div[@class="item-title"]')
            site2=site.xpath('div[@class="item-detail"]/div[@class="item-rela"]/a')
            site3=site.xpath('div[@class="item-sales"]')

            name=site1.xpath('h3/a/text()').extract()
            describe=site1.xpath('span/text()').extract()
            level=site2.xpath('div[@class="score-num"]/text()').extract()
            price=site3.xpath('div[@class="price price-now"]/a/text()').extract()

            # print(name)
            item['name'] = self.str_join([d.encode('utf-8') for d in name])
            item['describe'] = self.str_join([d.encode('utf-8') for d in describe])
            item['level'] = self.str_join([d.encode('utf-8') for d in level])
            item['price'] = self.str_join([d.encode('utf-8') for d in price])
            items.append(item)
            logging.info("Appending item "+item['name'])
        logging.info("Append done.")
        return items
    def str_join(self,strList):
        x=""
        for y in strList:
            x+=y
        return x





