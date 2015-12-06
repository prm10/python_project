__author__ = 'prm14'
import scrapy

class MobileSpider(scrapy.Spider):
    name="http://product.pconline.com.cn/mobile/"
    allowed_domains = ["product.pconline.com.cn/mobile/"]
    start_urls = [
        "http://mobile.pconline.com.cn/",
        "http://product.pconline.com.cn/mobile/"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

