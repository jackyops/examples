#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/26 12:43'

import requests,time

url = "https://hfjk.hfsmrz.com//robots.txt"
head = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',

]

def test1():
    global now_count
    httpClient = None
    try:
        httpClient = requests.request('get','https://hfjk.hfdatas.com/super/login.html')
        print('返回码:',httpClient.status_code)
        print('返回数据:',httpClient.text)

    except Exception as e:
        print(e)

    finally:
        if httpClient:
            httpClient.close()

def test2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    try:
        #httpClient = requests.request('get', 'https://hfjk.hfsmrz.com/super/login.html',headers=headers)
        httpClient = requests.request('get', url,headers=headers)
        print('返回状态码:', httpClient.status_code)
        #print('返回数据:', httpClient.text)
    except Exception as e:
        print(e)

    finally:
        if httpClient:
            httpClient.close()

def main():
    for i in range(5):
        print("请求%s次" % int(i+1))
        time.sleep(1)
        test2()





if __name__ == '__main__':
    main()
    #test2()

