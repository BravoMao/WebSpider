# -*- coding: utf-8 -*-
#encoding:utf-8
import requests
from lxml import html
class Zhihu_Spider():

    '''
    basic crawler
    '''

    def __init__(self,url,option="print_data_out"):
        '''
        initialize the crawler
        '''

        self.option=option
        self.url=url
        self.header={}
        self.header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"
#        self.header["Host"]="www.zhihu.com"
        self.header["Referer"]="www.zhihu.com"


        #cookie
        self.cookies={"z_c0":'"QUFEQTU0Z2VBQUFYQUFBQVlRSlZUWURFTEZlVW9kM3lIOElHQUc4QWpxSVVwRnVpNG5jemdBPT0=|1459959682|f7e446cdc4b6272a3c25c9763a0bc69943a8794c"',
                "unlock_ticket":'QUZDQUp3czV3QWtYQUFBQVlRSlZUZnBxQ2xmSWNXX3NuVXo3SVJleUM5Uy1BLUpEdXJEcEpBPT0',
                "login":'"NDc3ZDA0OTU5ZTc0NGE5MmE3ZGRjOTk0MGRiZmI0YmI=|1459956598|064e3ed29a18461ebaf69e421596bbdd2aa8659d"',
                "n_c":"1",
                "q_c1":"efbabc1e9aef4c348876907a25379c6e|1458811078000|1458811078000",
                "l_cap_id":'"MWRjOWM3ZmY0ZWM2NDdjZGFlZGM1MjhmZDIwMDk0YTg=|1459959674|9b8201da83d29abb20cf8d31343bc1d03010353c"',
                "d_c0":'"AHAABU4OqgmPTiYCZouX3Ei-2CHF6FppTVw=|1458811079"',
                "cap_id":'"MTNlYThmNjc1N2ZhNDEwNjhmMjhmMmYzMTljNTcwMzQ=|1459959674|bfd74e4e8b06547ec378f53b6b3abaf511e9c175"'}

    def send_request(self):
        '''
        send a request to get HTML source
        '''
        added_followee_url=self.url+"/followees"
        try:
            r=requests.get(added_followee_url,cookies=self.cookies,headers=self.header,verify=False)
        except:
            return

        content=r.text

        print(content)


        if r.status_code==200:
            self.parse_user_profile(content)

    def process_xpath_source(self,source):
        if source:
            return source[0]
        else:
            return ''

    def parse_user_profile(self,html_source):
        '''
        parse the user's profile to mongo
        '''

        #initialize variances

        self.user_name=''
        self.fuser_gender=''
        self.user_location=''
        self.user_followees=''
        self.user_followers=''
        self.user_be_agreed=''
        self.user_be_thanked=''
        self.user_education_school=''
        self.user_education_subject=''
        self.user_employment=''
        self.user_employment_extra=''
        self.user_info=''
        self.user_intro=''

        tree=html.fromstring(html_source)

        #parse the html via lxml
        self.user_name=self.process_xpath_source(tree.xpath("//a[@class='name']/text()"))
        self.user_location=self.process_xpath_source(tree.xpath("//span[@class='location item']/@title"))
        self.user_gender=self.process_xpath_source(tree.xpath("//span[@class='item gender']/i/@class"))
        if "female" in self.user_gender and self.user_gender:
            self.user_gender="female"
        else:
            self.user_gender="male"
        self.user_employment=self.process_xpath_source(tree.xpath("//span[@class='employment item']/@title"))
        self.user_employment_extra=self.process_xpath_source(tree.xpath("//span[@class='position item']/@title"))
        self.user_education_school=self.process_xpath_source(tree.xpath("//span[@class='education item']/@title"))
        self.user_education_subject=self.process_xpath_source(tree.xpath("//span[@class='education-extra item']/@title"))
        try:
            self.user_followees=tree.xpath("//div[@class='zu-main-sidebar']//strong")[0].text
            self.user_followers=tree.xpath("//div[@class='zu-main-sidebar']//strong")[1].text
        except:
            return

        self.user_be_agreed=self.process_xpath_source(tree.xpath("//span[@class='zm-profile-header-user-agree']/strong/text()"))
        self.user_be_thanked=self.process_xpath_source(tree.xpath("//span[@class='zm-profile-header-user-thanks']/strong/text()"))
        self.user_info=self.process_xpath_source(tree.xpath("//span[@class='bio']/@title"))
        self.user_intro=self.process_xpath_source(tree.xpath("//span[@class='content']/text()"))

        if self.option=="print_data_out":
            self.print_data_out()
        else:
            self.store_data_to_mongo()

        #find the follower's url
        url_list=tree.xpath("//h2[@class='zm-list-content-title']/a/@href")
        for target_url in url_list:
            target_url=target_url.replace("https","http")

    def print_data_out(self):
        '''
        打印用户信息
        '''

        print "*"*60
        print '用户名:%s\n' % self.user_name
        print "用户性别:%s\n" % self.user_gender
        print '用户地址:%s\n' % self.user_location
        print "被同意:%s\n" % self.user_be_agreed
        print "被感谢:%s\n" % self.user_be_thanked
        print "被关注:%s\n" % self.user_followers
        print "关注了:%s\n" % self.user_followees
        print "工作:%s/%s" % (self.user_employment,self.user_employment_extra)
        print "教育:%s/%s" % (self.user_education_school,self.user_education_subject)
        print "用户信息:%s" % self.user_info
        print "*"*60

if __name__ == "__main__":
    zhihuUser=Zhihu_Spider("https://www.zhihu.com/people/BravoMaooo")
    zhihuUser.send_request()
    zhihuUser.print_data_out()