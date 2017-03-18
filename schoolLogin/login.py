#!/usr/bin/python
# coding=utf-8

import urllib2


def post(url):
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
    # req.add_header('Cookie', 'tunet=yuanwq14%0Aywq%40hyq; thuwebcookie=2043441062.20480.0000')
    req.add_header('Connection', 'keep-alive')

    #data = 'action=login&username=prm14&password={MD5_HEX}61db7feedb460e622bcc617223a8ce9f&ac_id=1'
	data = 'action=login&username=yuanwq14&password={MD5_HEX}c2e6a66962a2a38c1a65861f1ce9b513&ac_id=1'
    print(data)
    # enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()


def main():
    posturl = "http://net.tsinghua.edu.cn/do_login.php"
    print post(posturl)


if __name__ == '__main__':
    main()
