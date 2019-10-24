import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
}

link = 'https://pv.sohu.com/cityjson'
url1 = 'https://www.tianqiapi.com/api/'
url2 = url1 + '?version=v6&ip=223.6.6.6&appid=22441771&appsecret=jook9nFg'


def get_city_code(url):
    response = requests.get(url, headers=header)
    response_1 = response.text.rsplit('var returnCitySN = ')[1]
    response_dict = response_1.rsplit(';')[0]
    city_code = eval(response_dict)['cid']
    # return city_code
    # print(city_code)


def get_weather(url2):
    response = requests.get(url2, headers=header)
    response_dict = eval(response.text)
    response_list = list(response_dict.values())
    num_list = [1, 2, 4, 8, 13, 14, 21, 22]
    for x in num_list:
        print(response_list[x])


# get_city_code(link)
get_weather(url2)


# https://fleet.mdihi.com/chat/chatClient/chatbox.jsp?companyID=365030391&configID=1489&jid=6765387387&s=1
