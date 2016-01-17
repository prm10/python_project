#!/usr/bin/python
#coding=utf-8
import urllib
import urllib2
def post(url, data):
    req = urllib2.Request(url)
    req.add_header('Host', 'net.tsinghua.edu.cn')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0')
    req.add_header('Accept', '*/*')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')
    req.add_header('Accept-Encoding', 'gzip, deflate')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    req.add_header('Referer', 'http://net.tsinghua.edu.cn/wired/')
    req.add_header('Content-Length', '89')
    req.add_header('Cookie', 'tunet=yuanwq14%0Aywq%40hyq; thuwebcookie=2043441062.20480.0000')
    req.add_header('Connection', 'keep-alive')

    data = 'action=login&username=yuanwq14&password={MD5_HEX}c2e6a66962a2a38c1a65861f1ce9b513&ac_id=1'#urllib.urlencode(data)
    print(data)
    #enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()
def main():
  posturl = "http://net.tsinghua.edu.cn/wired/"
  data = {'ac_id': '1',
          'action': 'login',
          'password': '{MD5_HEX}c2e6a66962a2a38c1a65861f1ce9b513',
          'username': 'yuanwq14'
          }
  print post(posturl, data)
if __name__ == '__main__':
  main()

'''

url1 = "http://net.tsinghua.edu.cn"

host="net.tsinghua.edu.cn"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'
headers = {'User-Agent': user_agent}
request = urllib2.Request(url1)
response = urllib2.urlopen(request)
webPage = response.read().decode('gbk', "ignore")
response.close()


'Accept-Encoding','gzip, deflate'
Accept-Language
zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
'Connection','keep-alive'
Content-Length
89
Content-Type
application/x-www-form-urlencoded; charset=UTF-8
Cookie
tunet=yuanwq14%0Aywq%40hyq; thuwebcookie=2043441062.20480.0000
Host
net.tsinghua.edu.cn
Referer
http://net.tsinghua.edu.cn/wired/
'User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'
X-Requested-With
XMLHttpRequest
'''
