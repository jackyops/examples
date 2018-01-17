# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/10/26 11:35'

import sys
import time
import threading
import requests
import random
import uuid
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='测试脚本日志.log',
                    filemode='w')

add="192.168.5.10"
port = 80
thread_count = 15   #单次并发数量
request_interval = 10   #请求间隔(秒)
test_count = 10   # 指定测试次数

now_count = 0

lock_obj = threading.Lock()

def send_http():
    global now_count
    httpClient = None

    try:
        httpClient = requests.request('get','http://api.zkteco.com/admin/a.html')

        print('返回码:',httpClient.status_code)
        print('返回数据:',httpClient.text)

        logging.info('返回码:' + httpClient.status_code)
        logging.info('返回数据:' + httpClient.text)

        sys.stdout.flush()
        now_count += 1

    except Exception as e:
        print(e)
        logging.info(e)

    finally:
        if httpClient:
            httpClient.close()


def test_func(run_count):
    global now_count
    global request_interval
    global lock_obj
    cnt = 0

    while cnt < run_count:
        lock_obj.acquire()
        print('')
        print('***************************请求次数:' + str(now_count) + '*******************************')
        print('Thread:(%d) Time:%s\n'%(threading.get_ident(), time.ctime()))

        logging.info('')
        logging.info('***************************请求次数:' + str(now_count) + '*******************************')
        logging.info('Thread:(%d) Time:%s\n' % (threading.get_ident(), time.ctime()))

        cnt += 1
        send_http()
        sys.stdout.flush()
        lock_obj.release()
        time.sleep(request_interval)

def test(ct):
    global thread_count
    for i in range(thread_count):
        threading.Thread(target=test_func,args=(ct,))

if __name__ == '__main__':
    global test_count
    test(test_count)
    while True:
        time.sleep(100)





