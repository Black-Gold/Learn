import requests
from datetime import datetime, date, timedelta


# 20161228
def gen_dates(init_date, days):
    day = timedelta(days=1)
    for i in range(days):
        yield init_date + day * i


# ??url???????????????????pdf??
init_date = date(2016, 12, 28)
for url_date in gen_dates(init_date, 1000):
    url_date2 = datetime.strftime(url_date, '%Y%m%d')
    # print(url_date2)
    url1 = "http://www.xxx.com/"
    url2 = "/Zabbix_3_training_day.pdf"
    down_url = url1 + url_date2 + url2
    request = requests.get(down_url)
    if request.status_code == 200:
        print(down_url)
