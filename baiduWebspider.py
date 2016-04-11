#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string, urllib2

#定义百度函数
def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i,5) + '.html'#自动填充成六位的文件名
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'
        f = open(sName,'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()


#-------- 在这里输入参数 ------------------
bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))
begin_page = int(raw_input(u'请输入开始的页数：\n'))
end_page = int(raw_input(u'请输入终点的页数：\n'))

#-------- 在这里输入参数 ------------------


#调用
baidu_tieba(bdurl,begin_page,end_page)