import requests


def get_weather(url):
    # 定义http head伪装成curl浏览器获取IP数据
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",}
    request = requests.get(url, headers=headers)
    response = eval(request.text)
    print(response)


def get_mfw_news(url):
    # 定义http head伪装成curl浏览器获取IP数据
    headers = {'User-Agent': "curl/10.0",
               "Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/json"}
    request = requests.get(url, headers=headers)
    response = eval(request.text)
    print(response)


get_mfw_news('http://www.moji.com/mojiweather/news.php')
get_weather('http://www.moji.com/mojiweather/forecast.php')
