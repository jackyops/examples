# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/18 21:12'

import requests
import time

url = 'https://api.live.bilibili.com/ajax/msg'

# 定义提供的数据
dat = {'roomid':544893,
       'token':'',
       'csrf_token':''}
while True:
    time.sleep(2)
    html1 = requests.post(url,data=dat)
    # 切片操作提起数据
    asd1 = list(map(lambda i:html1.json()['data']['room'][i]['text'],range(10)))

    time.sleep(2)
    html2 = requests.post(url, data=dat)
    asd2= list(map(lambda i: html2.json()['data']['room'][i]['text'], range(10)))

    asd = list(set(asd1 + asd2))
    print(asd)

#print(html.json())