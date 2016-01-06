import urllib2

response = urllib2.urlopen("http://www.jianlizhang.com")
print response.read()