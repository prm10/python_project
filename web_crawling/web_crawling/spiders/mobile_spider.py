__author__ = 'prm14'
import scrapy
from scrapy import Selector
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
        for site in sites:
            item=WebCrawlingItem()
            site1=site.xpath('/div[@class="item-detail"]/div[@class="item-title"]')
            name=site1.xpath('/h3/a/text()').extract()
            decribe=site1.xpath('/span/text()').extract()
            site2=site.xpath('/div[@class="item-detail"]/div[@class="item-rela"]/a')
            level=site2.xpath('/div[@class="score-num"]/text()').extract()
            site3=site.xpath('/div[@class="item-sales"]')
            price=site3.xpath('/div[@class="price price-now"]/a/text()').extract()







