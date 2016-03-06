#!/usr/bin/python
# coding=utf-8

# targetIP=166.111.73.
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt=socket(AF_INET, SOCK_STREAM)
        connSkt.settimeout(3)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.settimeout(None)
        print(tgtHost+"/tcp open")
    except:
        print(tgtHost+"/tcp closed")

# tgtIP=gethostbyname('www.baidu.com')
# print(tgtIP)
# connScan(tgtHost, int(port))

ip_array=[166,111,73,1]
# ip_str=".".join(map(str,ip_array))
for i in range(1,255):
    ip_array[3]=i
    ip_str=".".join(map(str,ip_array))
    # print(ip_str)
    connScan(ip_str, 3389)