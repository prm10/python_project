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

# ip_array=[166,111,138,1]
ip_array=[59,66,214,1]
port=22
for i in range(2,255):
    ip_array[3]=i
    ip_str=".".join(map(str,ip_array))
    connScan(ip_str, port)