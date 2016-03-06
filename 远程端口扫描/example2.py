# -*- coding: utf-8 -*-
__author__ = 'prm14'
import wmi

ip = "192.168.1.13"
username = "prm14"
password = "prm10"
from socket import *
try:
    print "Establishing connection to %s" %ip
    connection = wmi.WMI(ip, user=username, password=password)
    print "Connection established"
except wmi.x_wmi:
    print "Your Username and Password of "+getfqdn(ip)+" are wrong."