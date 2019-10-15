#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import requests
from bs4 import BeautifulSoup

'''
从https://www.biqukan.com网站抓取小说
下载小说一念永恒

'''


class downloader(object):
    def __init__(self):
        self.domain = 'http://www.biqukan.com/'
        self.link = 'http://www.biqukan.com/1_1094/'
        self.name = []  # 存放章节名称
        self.urls = []   # 存放章节链接
        self.num = []   # 存放章节数

    # 获取下载链接
    def get_down_url(self):
        r = requests.get(url=self.link)
        html = r.text
        zj_div = BeautifulSoup(html)
        div = zj_div.find_all(attrs={'div', 'listmain'}, recursive=True)
        zj_a = BeautifulSoup(str(div[0]))
        a = zj_a.find_all(name='a')
        self.num = len(a[15:])  # 剔除不必要的章节并统计章节数

        for everyone in a[15:]:
            self.name.append(everyone.string)
            self.urls.append(self.domain + everyone.get('href'))

    # 获取下载章节内容
    def get_content(self, target):
        r = requests.get(url=target)
        html = r.text
        bs = BeautifulSoup(html)
        texts = bs.find_all(attrs={'div', 'showtxt'})
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    # 将小说写入到文件,文件默认保存在脚本文件的当前路径下
    def novel_writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

# 单进程跑，没有开进程池。下载速度略慢
if __name__ == "__main__":
    down = downloader()
    down.get_down_url()
    print('开始下载...')
    for i in range(down.num):
        down.novel_writer(down.name[i], '一念永恒.txt',
                          down.get_content(down.urls[i]))
        sys.stdout.write("已下载：%.3f%%" % float(i/down.num) + '\r')
        sys.stdout.flush()
    print('下载完成！！！')
