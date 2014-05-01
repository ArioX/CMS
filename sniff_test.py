#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def audit(url, head, body):
    if re.search('<input[^>]+type=[\'"]*file[\'"]*', body, re.I):
        security_note(url)

if __name__ == '__main__':
    from dummy import *
    s='''
<input type="file" name="FileUploadbiao" id="FileUploadbiao"/></td>
'''
    audit('http://www.baidu.com/', '200', s)

