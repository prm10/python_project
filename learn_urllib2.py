#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'prm14'
import urllib2
from lxml import etree
import re


class CrawlingUsingUrllib2(object):
    def __init__(self):
        self.file = file('pconline.txt', 'w')
        self.file.write("")
        self.file.close()
        self.file = file('pconline.txt', 'a')

        self.doneUrl = set()
        self.maxEcho = 1000
        self.mobileIdSet = set()

    def __del__(self):
        self.file.close()

    def setStartUrls(self, urls):
        self.start_urls = urls

    def setAllowedDomains(self, domains):
        self.allowed_domains = domains

    def setMaxEcho(self, num):
        self.maxEcho = num

    def write2txt(self, info, f):
        f.write(info.encode('utf-8') + '\r\n')

    def run(self):
        self.restUrl = set(self.start_urls)
        while (len(self.restUrl) > 0):
            url1 = self.restUrl.pop()
            response = urllib2.urlopen(url1)
            webPage = response.read().decode('GBK','ignore')
            response.close()
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

                self.write2txt('name: ' + name, self.file)
                self.write2txt('url: ' + url2, self.file)
                self.write2txt('level: ' + level, self.file)
                self.write2txt('price: ' + price, self.file)
                urlComment = url2[0:len(url2) - 5] + '_comment' + url2[len(url2) - 5:len(url2)]
                self.getComment(urlComment)
                self.write2txt('', self.file)
            self.doneUrl.add(url1)
            print(str(len(self.doneUrl)) + " urls have been found")
            if len(self.doneUrl) > self.maxEcho: break
            nextUrl = sel.xpath('//a[@class="page-next"]/@href')
            if (len(nextUrl) > 0):
                url3 = nextUrl[0]
                url3 = self.allowed_domains[0] + url3.encode('utf-8')
                print(url3)
                if url3 not in self.doneUrl:
                    self.restUrl.add(url3)

    def getComment(self, urlComment):
        url1 = urlComment
        pattern = re.compile('\/(\d+)')
        mobileId = pattern.findall(url1)[-1]
        if mobileId in self.mobileIdSet: return
        else:self.mobileIdSet.add(mobileId)
        pageNo = 0
        while True:
            pageNo += 1
            print("%d,%d"%(len(self.mobileIdSet),pageNo))
            url1 = "http://pdcmt.pconline.com.cn/front/2015/mtp-list.jsp?productId=%s&filterBy=-1&itemCfgId=-1&order=2&pageNo=%d" % (
                mobileId, pageNo)
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'
            headers = {'User-Agent': user_agent}
            request = urllib2.Request(url1)
            response = urllib2.urlopen(request)
            webPage = response.read().decode('gbk', "ignore")
            response.close()
            sel = etree.HTML(webPage)
            if sel is None: break
            sites = sel.xpath('//dl[@class="cmt-content"]')
            for site in sites:
                site1 = site.xpath('dd[@class="cmt-detail"]//li/text()')
                for comment in site1:
                    self.write2txt('#' + comment.replace(u'\xa0', u' '), self.file)
                site2 = site.xpath('dd[@class="cmt-detail"]//p[@class="text"]/text()')
                for comment in site2:
                    self.write2txt('#' + comment.replace(u'\xa0', u' '), self.file)
                site3 = site.xpath('dd[@class="cmt-reply-box"]//p[@class="reply-texts"]/text()')
                for comment in site3:
                    self.write2txt('##' + comment.replace(u'\xa0', u' '), self.file)


a = CrawlingUsingUrllib2()
a.setStartUrls(['http://product.pconline.com.cn/mobile/25s1.shtml'])#(["http://product.pconline.com.cn/mobile/"])
a.setAllowedDomains(["http://product.pconline.com.cn"])
a.run()

# url1 = "http://product.pconline.com.cn/mobile/apple/539007_comment.html"
# pattern = re.compile('\/(\d+)')
# mobileId = pattern.findall(url1)[0]
# print(mobileId)
# pageNo = 3
# while True:
#     pageNo += 1
#     print('***********************************************'+str(pageNo))
#     url1 = "http://pdcmt.pconline.com.cn/front/2015/mtp-list.jsp?productId=%s&filterBy=-1&itemCfgId=-1&order=2&pageNo=%d" % (
#         mobileId, pageNo)
#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'
#     headers = {'User-Agent': user_agent}
#     request = urllib2.Request(url1, headers=headers)
#     response = urllib2.urlopen(request)
#     webPage = response.read().decode('gbk',"ignore")
#     sel = etree.HTML(webPage)
#     if sel is None: break
#     sites = sel.xpath('//dl[@class="cmt-content"]')
#     for site in sites:
#         site1 = site.xpath('dd[@class="cmt-detail"]//li/text()')
#         for comment in site1:
#             print('\t' + comment.replace(u'\xa0', u' '))
#         site2 = site.xpath('dd[@class="cmt-detail"]//p[@class="text"]/text()')
#         for comment in site2:
#             print('\t' + comment.replace(u'\xa0', u' '))
#         site3 = site.xpath('dd[@class="cmt-reply-box"]//p[@class="reply-texts"]/text()')
#         for comment in site3:
#             print('\t\t' + comment.replace(u'\xa0', u' '))
