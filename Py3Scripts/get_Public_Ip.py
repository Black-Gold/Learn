"""
# 基于Python3、requests
# 获取公网ip方式一
from json import load
from urllib.request import urlopen

public_ip = load(urlopen("http://jsonip.com"))["ip"]
print(public_ip)
"""


# import re
# import requests
#
# link = urllib.urlopen("http://txt.go.sohu.com/ip/soip")
# text = link.read()
# public_ip = re.findall(r'\d+.\d+.\d+.\d+', text)
# print(public_ip[0])


"""
# 基于Python3、requests
# 输出ip为bytes类型
# 获取公网ip方式二
from urllib.request import urlopen

public_ip = urlopen("http://ip.42.pl/raw").read()
print(public_ip)
"""

"""
from json import load
from urllib.request import urlopen

public_ip = load(urlopen("http://httpbin.org/ip"))["origin"]
print(public_ip)
"""


"""
# 利用阿里获取公网IP
import requests

url = 'https://amdc.alipay.com/squery'

headers = {
    'Host': 'amdc.alipay.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
}
response = requests.get(url, headers=headers)
print(eval(response.text)['clientIp'])

"""