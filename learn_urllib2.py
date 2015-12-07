__author__ = 'prm14'

import urllib2
#
response = urllib2.urlopen("http://product.pconline.com.cn/mobile/")
# print response.read()

import scrapy
sel = scrapy.Selector(response)
