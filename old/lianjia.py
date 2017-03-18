# -*- coding: utf-8 -*-
__author__ = 'prm14'
import urllib2
from lxml import etree
import re
import zlib

url1='http://bj.lianjia.com/xiaoqu/pg100/'#'http://bj.lianjia.com/xiaoqu/pg100/'
req = urllib2.Request(url1)
# req.add_header('Accept-Encoding', 'gzip, deflate')
response = urllib2.urlopen(url1)
webPage = response.read()
# webPage = zlib.decompress(response.read(), 16+zlib.MAX_WBITS)
response.close()
f = file('lianjiaHTML.txt', 'w')
f.write("")
f.close()
f = file('lianjiaHTML.txt', 'a')
f.write(webPage)
f.close()