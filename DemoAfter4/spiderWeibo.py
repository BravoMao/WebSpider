import requests
import re

user_agent = {'User-agent': 'spider'}
r = requests.get("http://www.weibo.com/2714155200",headers=user_agent)
p_nick = re.compile(r"<title>(.*?)")
m_nick = re.findall(p_nick,r.text)
if len(m_nick) == 1:
    print m_nick[0]
else:
    print "Not found!"