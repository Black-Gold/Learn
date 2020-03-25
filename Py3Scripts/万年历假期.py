from urllib.request import urlopen, Request
import ssl
import json

host = 'https://jisuwnl.market.alicloudapi.com'
# path = '/calendar/holiday'
path = '/calendar/query'
method = 'GET'
appcode = '32394ce559ff4551936f79a7ea8237f0'
querys = 'date=2020-03-12'
bodys = {}
# url = host + path
url = host + path + '?' + querys

request = Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urlopen(request, context=ctx)
content = response.read()
content_dict = json.loads(content.decode('utf-8'))
# print(content_dict['result']['2019-10-01']['content'])
print(content_dict['result'])

"""
输出格式

{'status': 0, 'msg': 'ok',
'result': {'2018-12-30': {'name': '元旦', 'content': '12月30日至1月1日放假，共三天，与周末连休。'},
'2019-02-04': {'name': '春节', 'content': '2月04日至2月10日放假调休，共7天。2月2日（周六）、2月3日（周日）上班。'},
'2019-04-05': {'name': '清明节', 'content': '4月5日至7日放假调休，共3天，与周末连休。'},
'2019-05-01': {'name': '劳动节', 'content': '无调休，共1天。'},
'2019-06-07': {'name': '端午节', 'content': '6月07日至09日放假，共3天，与周末连休。'},
'2019-09-13': {'name': '中秋节', 'content': '9月13日至15日放假，共3天，与周末连休。'},
'2019-10-01': {'name': '国庆节', 'content': '10月1日至7日放假调休，共7天。9月29日（周日）、10月12日（周六）上班。'}}}
"""
