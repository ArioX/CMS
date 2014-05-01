#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'
#
# Vulnerable Files :
#/list.php?tid=[sql]
#/members.php?id=[sql]
#/book.php?id=[sql]


import re
import urllib2

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg

    _, head, body, _, _ = curl.curl(url + '')
    if body and body.find('2e0e20673083dea5cc87a85d54022049') != -1:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://localhost/dedecms/5.6final/')[1])