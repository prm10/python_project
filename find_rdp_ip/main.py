#!/usr/bin/python
# coding=utf-8

from socket import *

def connScan(tgtIP, tgtPort):
    try:
        connSkt=socket(AF_INET, SOCK_STREAM)
        connSkt.settimeout(0.1)
        connSkt.connect((tgtIP, tgtPort))
        connSkt.settimeout(None)
        print("%s:%s/tcp open"%(tgtIP,tgtPort))
    except:
        return
        # print(tgtIP+"/tcp closed")

# tgtIP=gethostbyname('www.baidu.com')
# print(tgtIP)
# connScan(tgtHost, int(port))

ip_array=[166,111,73,1]
# ip_str=".".join(map(str,ip_array))
for i in range(2,255):
    ip_array[3]=i
    ip_str=".".join(map(str,ip_array))
    # print(ip_str)
    connScan(ip_str, 2333)