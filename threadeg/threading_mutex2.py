#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/2/23 20:13'

import threading,time


def addNum():
    global num
    print('--get num:',num)
    time.sleep(1)
    # 修改数据前加锁
    lock.acquire()
    num -= 1
    lock.release()  # 修改后释放
    print(num)

num = 100
thread_list = []
lock = threading.Lock()  #生成全局锁
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

#等待所有线程执行完毕
for t in thread_list:
    t.join()

print('final num:',num)


