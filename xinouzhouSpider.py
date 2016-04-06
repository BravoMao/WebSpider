#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string,urllib2,re
def xinouzhou(url,begin_page,end_page):
    f = open('test.txt','wb')
    for i in range(begin_page, end_page+1):
        m = urllib2.urlopen(url + str(i)).read()
        matches = re.findall(r']</em><a href=\"(.*?)\" onclick=\"atarget\(this\)\" class=\"s xst\">(.*?)</a>',m,re.DOTALL)

        #matches = re.findall(r'<img src=(.*)>',m,re.DOTALL)
        for st in matches:
            if "defense" in st[1]:
                print(st[1])
                f.write(st[1]+' ')
                f.write(st[0]+'\n')


xinouzhou('http://buy.xineurope.com/forum.php?mod=forumdisplay&fid=10&cityid=1&typeid=18&filter=cityid&cityid=1&typeid=18&page=',1,10)