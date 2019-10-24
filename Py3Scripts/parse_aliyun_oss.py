import xml.etree.ElementTree as ET
import requests
import json
import re
import os

# 请求解析url
url = 'http://xxx.oss-cn-hangzhou.aliyuncs.com'
request = requests.get(url)
response = request.text
# print(response)

# xml解析
tree = ET.ElementTree(ET.fromstring(response))
root = tree.getroot()
# print(root.attrib)

for content in root.findall('Contents'):
    key = content.find('Key').text
    full_url = url + key
    request = requests.get(full_url)
    content_type = request.headers.get('content-type')
    # print(content_type)
    if 'octet-stream' not in content_type:
        # print(full_url)
        filename = os.path.basename(full_url)
        # print(filename)
        local_path = '本地路径'
        open(local_path + filename, 'wb').write(request.content)
