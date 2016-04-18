import requests
r = requests.get('https://api.github.com/user', auth=('login', 'pwd'))
print(r.json())

#get
params= {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=params)
'''
>>> print(r.url)
http://httpbin.org/get?key2=value2&key1=value1
'''
#post
body = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=body)
'''
>>> print(r.text)
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
'''