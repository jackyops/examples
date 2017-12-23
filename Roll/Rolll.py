# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/23 21:16'

'''
Title： bilibili网站发射弹幕

'''

import requests
import time
import configparser
import random

# 文件对象
target = configparser.ConfigParser()

#读取文件
target.read('E:\zyc\Projects\examples\examples\Roll\sgg.ini',encoding='utf8')


url = 'https://interface.bilibili.com/dmpost?cid=28421902&aid=17398733&pid=1&ct=1'

# 帐号信息
cookie = {
    'Cookie':''
}

while True:
    message = target['我的弹幕'][str(random.randint(1,5))]
    # 提交的数据，字典JSON/TXT
    form = {
        'fontfize':'25',
        'pool':'0',
        'mode':'1',
        'color':'16777215',
        'rnd':str(time.time()*1000000),
        'message':'222',
        'playTime':'0.08',
        'cid':'2841902',
        'date': time.strftime("%Y-%m-%d +%X",time.localtime()),
        'csrf':'124324235353453452',
    }
    requests.request('POST',url,data = form,cookie = cookie)
    time.sleep(5)

