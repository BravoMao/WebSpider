import urllib2

response = urllib2.urlopen("http://www.google.com")
print response.read()