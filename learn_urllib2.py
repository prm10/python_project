#!/usr/bin/env python
# -*- coding:utf8 -*-
__author__ = 'prm14'
import urllib2
import StringIO
import gzip
from lxml import etree


class CrawlingUsingUrllib2(object):
    def __init__(self):
        self.file = file('pconline.txt', 'w')
        self.file.write("")
        self.file.close()
        self.file = file('pconline.txt', 'a')
        self.doneUrl = set()
        self.maxEcho = 1000

    def __del__(self):
        self.file.close()

    def setStartUrls(self, urls):
        self.start_urls = urls

    def setAllowedDomains(self, domains):
        self.allowed_domains = domains

    def setMaxEcho(self, num):
        self.maxEcho = num

    def write2txt(self, info):
        self.file.write(info.encode('utf-8') + '\r\n')

    def run(self):
        self.restUrl = set(self.start_urls)
        while (len(self.restUrl) > 0):
            # print("Append begin.")
            url1 = self.restUrl.pop()
            response = urllib2.urlopen(url1)
            webPage = response.read().decode('gbk')
            sel = etree.HTML(webPage)
            sites = sel.xpath('//li[@class="item"]/div[@class="item-wrap"]')

            for site in sites:
                site1 = site.xpath('div[@class="item-detail"]/div[@class="item-title"]')[0]
                site2 = site.xpath('div[@class="item-detail"]/div[@class="item-rela"]/a')[0]
                site3 = site.xpath('div[@class="item-sales"]')[0]

                name = site1.xpath('h3/a/text()')[0]
                url2 = site1.xpath('h3/a/@href')[0]
                level = site2.xpath('div[@class="score-num"]/text()|span[@class="score-none"]/text()')[0]
                price = site3.xpath('div/a/text()')[0]

                # print(name)
                # str_join = lambda x, y: x + y
                self.write2txt('name: ' + name)
                self.write2txt('url: ' + url2)
                self.write2txt('level: ' + level)
                self.write2txt('price: ' + price)
                self.write2txt('')
            self.doneUrl.add(url1)
            print(str(len(self.doneUrl)) + " urls have been found")
            if len(self.doneUrl) > self.maxEcho: break
            nextUrl=sel.xpath('//a[@class="page-next"]/@href')
            if(len(nextUrl)>0):
                url3 =nextUrl[0]
                url3= self.allowed_domains[0]+url3.encode('utf-8')
                print(url3)
                if url3 not in self.doneUrl:
                    self.restUrl.add(url3)


a = CrawlingUsingUrllib2()
a.setStartUrls(["http://product.pconline.com.cn/mobile/"])
a.setAllowedDomains(["http://product.pconline.com.cn"])
a.run()

# url="http://product.pconline.com.cn/mobile/"
# response = urllib2.urlopen(url)
# webPage=response.read().decode('gbk')
# sel=etree.HTML(webPage)
# sites=sel.xpath('//li[@class="item"]/div[@class="item-wrap"]/div[@class="item-detail"]/div[@class="item-title"]/h3/a/text()')
# print(str(len(sites))+' sites found')
# for s in sites:
#     print(s)
