#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/2/24 15:11'

import threading
import queue


def producer():
    for i in range(20):
        q.put("包子 %s" % i)
    print("开始等待所有的包子被取走...")
    q.join()
    print("所有的包子被取完了...")

def consumer(n):
    while q.qsize() > 0:
        print("%s 取到" %n, q.get())
        q.task_done()   #告知这个任务执行完了

q = queue.Queue()
p = threading.Thread(target=producer,)
p.start()


#c1 = consumer("Jacky")
consumer("Jacky")