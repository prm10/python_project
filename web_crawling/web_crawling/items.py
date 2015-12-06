# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebCrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()  # 手机型号
    price = scrapy.Field()  # 价格
    commentNum = scrapy.Field  # 评论数
    commentLevel = scrapy.Field  # 评论等级
    publishTime = scrapy.Field  # 发行时间
