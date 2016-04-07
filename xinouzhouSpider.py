#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string,urllib2,re,threading

class xinouzhouThread (threading.Thread):
    def __init__(self, threadID, name, url,index,file):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url=url
        self.index=index
        self.file=file
    def run(self):
        print "Starting " + self.name
        readHtml(self.url,self.index,self.file)
        print "Exiting " + self.name

def xinouzhouSpider(url,begin_page,end_page):
    f = open('C:/Users/jzhang/PycharmProjects/WedSpiderTutorial/test.txt','wb')
    for i in range(begin_page, end_page+1):
        thread = xinouzhouThread(1, "Thread-"+str(i), url,i,f)
        thread.start()
    print "Exiting Main Thread"

def readHtml(url,index,file):
     m = urllib2.urlopen(url + str(index)).read()
     matches = re.findall(r']</em><a href=\"(.*?)\" onclick=\"atarget\(this\)\" class=\"s xst\">(.*?)</a>',m,re.DOTALL)

     #matches = re.findall(r'<img src=(.*)>',m,re.DOTALL)
     for st in matches:
        if "defense" in st[1]:
            print(st[1])
            file.write(st[1]+' ')
            file.write(st[0]+'\n')

if __name__ == "__main__":
    xinouzhouSpider('http://buy.xineurope.com/forum.php?mod=forumdisplay&fid=10&cityid=1&typeid=18&filter=cityid&cityid=1&typeid=18&page=',1,10)