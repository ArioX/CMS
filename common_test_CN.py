#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
任务调度:
task_push(servie, arg, uuid=None, target=None), 新增加一个服务，后面是参数,比如
    task_push('www', 'http://www.baidu.com/')
    调度器会传递所有插件的audit函数('www', 'http://www.baidu.com/')这样的参数
    如果指定UUID，UUID将做为此任务的唯一标识，防止重复，如果不指定，系统将自动生成一个UUID
    如果指定target参数，新生的任务产生的报告所属的域名为target指定的值

报告函数:
通知: security_note(str)
提示: security_info(str)
警告: security_warning(str)
漏洞: security_hole(str)

util:
    is_ipaddr(str)  字串是否一个IP地址
    decode_html(head, body) 根据HTTP头和内容进行编码转换成utf-8编码
    urljoin(base, ref) URL组合，比如urljoin('http://www.baidu.com/', 'abc/../dd.html') 将返回http://www.baidu.com/dd.html
    html2text(body, head='') HTML转换为txt,如果指定head,尝试用decode_html解码后转换
    get_url_host(url) 得到URL域名，因为太经常用了，附带写上
    get_domain_root(url) 得到一个URL或者域名的根域名(内置TLD字典)
    str_ration(str1, str2)  比较两个文本的相似度，会根据长度自动选择最快匹配算法

curl:
     参考curl的一个纯python迷你版本，只支持HTTP一些协议，可代替urllib，参数具体意思参考curl命令行版本 http://curl.haxx.se/
	 [-I | -d DATA] [-A USER_AGENT] [-b COOKIE]
                     [--connect-timeout CONNECT_TIMEOUT] [-e REFERER]
                     [-H HEADER] [-i] [-m MAX_TIME]
                     [--max-filesize MAX_FILESIZE] [--mime-type MIME_TYPE]
                     [-L] [--max-redirs MAX_REDIRS] [-T] [--retry RETRY]
                     [--retry-delay RETRY_DELAY] [-u USER] [-X REQUEST]
                     <url>
    多加的一个--mime-type指，如果HTTP头的Content-Type查找不到--mime-type指定的字串时，抛出异常, 中断接收

返回5个参数:
    code:       http响应代码
    head:       http头
    body:       http内容
    errcode:    出错代码0为无错
    final_url:  重定向后的URL,如果不变说明没有重定向

错误代码:
    CURLE_OK = 0
    CURLE_COULDNT_CONNECT = 1
    CURLE_OPERATION_TIMEDOUT = 2
    CURLE_RECV_ERROR = 3
    CURLE_SEND_ERROR = 4
    CURLE_FILESIZE_EXCEEDED = 5
    CURLE_COULDNT_RESOLVE_HOST = 6
    CURLE_UNSUPPORTED_PROTOCOL = 7
    # custome error
    CURLE_ARG_ERROR = 8
    CURLE_MIME_ERROR = 9

例子:
    code, head, body, ecode, redirect_url = curl.curl('-L http://www.baidu.com')
    GET:
        curl.curl('http://www.abc.com/')
    HEAD:
        curl.curl('-H http://www.abc.com/')
    POST:
        curl.curl('-d user=abc&pass=ddd http://www.abc.com/')
    PUT:
        curl.curl('T -d "这是PUT的内容" http://www.abc.com/')
    Cookie:
        curl.curl('-b user=abc&pass=ddd http://www.abc.com/')
    Referer:
        curl.curl('-e http://www.google.com/ http://www.abc.com/')
    Flow Redirect:
        curl.curl('-L http://www.abc.com/')

    curl在获取网页过程中会自动接收cookie,第二次请求会附带上去，如果想清空
        curl.reset()
    ....
        
'''

if __name__ == '__main__':
    from dummy import *
    code, head, body, error, _ = curl.curl('http://www.baidu.com/')
    if error == curl.CURLE_OK:
        print "OK"

    print util.is_ipaddr('8.8.8.8')
    print util.decode_html(head, body).decode('utf-8')
    print util.urljoin('http://www.baidu.com/', 'abc/../dd.html')
    print util.html2text(body)
    print util.get_domain_root("www.baidu.com.cn")
    print util.get_domain_root("http://bbs.sina.com.tw")
    print util.str_ratio("good", "not good")
    task_push('www', 'http://www.baidu.com/')

