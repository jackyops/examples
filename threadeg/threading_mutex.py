#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/2/23 20:13'
# 注：不要在3.x上运行，不知为什么，3.x上的结果总是正确的，可能是自动加了锁
import threading,time


def addNum():
    global num
    print('--get num:',num)
    time.sleep(1)
    num -= 1
    print(num)

num = 100
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print('final num:',num)


