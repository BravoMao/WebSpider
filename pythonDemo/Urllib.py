import urllib
import urllib2
import cookielib
import re
import string


class SDU_Spider:
    # 申明相关的属性
    def __init__(self):
        self.loginUrl = 'http://jwxt.sdu.edu.cn:7777/pls/wwwbks/bks_login2.login'   # 登录的url
        self.resultUrl = 'http://jwxt.sdu.edu.cn:7777/pls/wwwbks/bkscjcx.curscopre' # 显示成绩的url
        self.cookieJar = cookielib.CookieJar()                                      # 初始化一个CookieJar来处理Cookie的信息
        self.postdata=urllib.urlencode({'stuid':'201100300428','pwd':'921030'})     # POST的数据
        self.weights = []   #存储权重，也就是学分
        self.points = []    #存储分数，也就是成绩
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))

    def sdu_init(self):
        # 初始化链接并且获取cookie
        myRequest = urllib2.Request(url = self.loginUrl,data = self.postdata)   # 自定义一个请求
        result = self.opener.open(myRequest)            # 访问登录页面，获取到必须的cookie的值
        result = self.opener.open(self.resultUrl)       # 访问成绩页面，获得成绩的数据
        # 打印返回的内容
        # print result.read()
        self.deal_data(result.read().decode('gbk'))
        self.calculate_date();

    # 将内容从页面代码中抠出来
    def deal_data(self,myPage):
        myItems = re.findall('<TR>.*?<p.*?<p.*?<p.*?<p.*?<p.*?>(.*?)</p>.*?<p.*?<p.*?>(.*?)</p>.*?</TR>',myPage,re.S)     #获取到学分
        for item in myItems:
            self.weights.append(item[0].encode('gbk'))
            self.points.append(item[1].encode('gbk'))

    #计算绩点，如果成绩还没出来，或者成绩是优秀良好，就不运算该成绩
    def calculate_date(self):
        point = 0.0
        weight = 0.0
        for i in range(len(self.points)):
            if(self.points[i].isdigit()):
                point += string.atof(self.points[i])*string.atof(self.weights[i])
                weight += string.atof(self.weights[i])
        print point/weight


#调用
mySpider = SDU_Spider()
mySpider.sdu_init()