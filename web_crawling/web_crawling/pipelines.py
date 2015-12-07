# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WebCrawlingPipeline(object):
    def __init__(self):
        self.file = file('pconline.txt','w')
        self.file.write("")
        self.file = file('pconline.txt','a')
    def process_item(self, item, spider):
        s='name: '+item['name']+\
          '\r\ndecribe: '+item['decribe']+\
          '\r\nlevel: '+item['level']+\
          '\r\nprice: '+item['price']
        self.file.write(s)
        return item
