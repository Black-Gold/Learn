# 到期时间2020-08-29
from urllib.request import urlopen, Request
import json

host = 'http://toutiao-ali.juheapi.com'
path = '/toutiao/index'
method = 'GET'
appcode = '32394ce559ff4551936f79a7ea8237f0'
querys = 'type=keji'
bodys = {}
url = host + path + '?' + querys


request = Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urlopen(request)
content = response.read()
content_dict = json.loads(content)
# print(content.decode('utf-8'))
print(content_dict)
