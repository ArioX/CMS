#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 可引用任意Python内置库
import urlparse
import re

def assign(service, arg):
    '''
     service 的值代表arg参数的类型:
       'www'       : arg为一个经过模糊过滤的链接, 如: http://www.abc.com/news.asp?id=10
       'www-form'  : arg为一个爬虫构造过的form表单的dict结构, 如:
                      {
                        'action': 'http://www.abc.com/login.asp', 
                        'inputs': [
                                {'type': u'text', 'name': u'login', 'value': 'test'}, 
                                {'type': u'password', 'name': u'password', 'value': 'test'}, 
                                {'type': u'radio', 'name': u'graphicOption', 'value': u'minimum'}
                                ],
                        'ref': 'http://www.abc.com/', 
                        'method': u'post'
                       }
            
       'ip'        : arg为一个IP地址, 如: 1.1.1.1
       'dns'       : arg为一个新发现的域名, 如bbs.abc.com 

       端口服务扫描插件为必选插件, 新增以下参数

       'ssh'       : arg为一个开放SSH服务的IP地址
       'ftp'       : arg为一个开放FTP服务的IP地址
       'mssql'     : arg为一个开放MSSQL服务的IP地址
       'mysql'     : arg为一个开放MySQL服务的IP地址
       'telnet'    : arg为一个开放Telnet服务的IP地址
       'vnc'       : arg为一个开放VNC服务的IP地址

       CMS识别插件新增以下参数:
       
       'discuz', 'phpwind', 'wordpress', 'dedecms', 'php168', ... 具体请看CMS识别插件的说明

       其它情况:
           插件通过task_push自定义的参数
    '''
    # 此句表始只接收链接参数 
    if service != "www": 
        return
    
    '''
    返回参数:
        参数1:
            是否接收了一个任务(True/False)

        参数2:
            要传给audit函数的参数(可以为任意类型)
            如果为列表,比如arg为[1,2,3], 则，系统自动视为三个任务，参数分别是1,2,3

        参数3:
            可选参数，指任务的UUID,可以为任意能转化为字串的参数，如果不写，系统以返回的arg和插件本身做为UUID，防止重复任务,
            比如返回 True, arg, 888, 指888做为UUID，如果UUID为固定的，也就是指这个插件只会触发一次,
            此参数在检测特定的漏洞比较有用，比如你只想检测PHP后缀的文件，有没有漏洞，只想检测一次，不想所有PHP文件都检测,
            就返回True, arg, 'php' 以'php'做为此任务的UUID
    '''
    arr = urlparse.urlparse(arg)
    # 由链接参数构造出robots.txt的一个URL
    return True, '%s://%s/robots.txt' % (arr.scheme, arr.netloc)
    

def audit(arg):
    '''
     arg 为 assign 返回的第二个值
    '''
    url = arg
    code, head, res, errcode, final_url = curl.curl(url)
    if code == 200:
        if re.search('Content\-Type:\s+[^\n]*text[^\n]+', head, re.M) and res.find('<') == -1:
            sensitive_info = ''
            for m in re.finditer('[^\r\n]+(admin|manage)[^\r\n]+', res, re.M | re.I):
                sensitive_info += m.group(0)
            sensitive_info = sensitive_info.strip()
            if sensitive_info:
                security_note(url + ' : ' + sensitive_info)
    

# 测试代码
if __name__ == '__main__':
    # 引入本地模拟环境
    from dummy import *
    audit(assign('www', 'http://www.discuz.net/')[1])
