#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/2/24 15:11'

# 通过Event来实现两个或多个线程间的交互，下面是一个红绿灯的例子，即起动一个线程做交通指挥灯，生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则

import threading,time
import random

def light():
    if not event.isSet():
        event.set()  #wait就不阻塞 #绿灯状态
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--green light on---\033[0m')
        elif count < 13:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count< 20:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            # 打开绿灯
            event.set()
        time.sleep(1)
        count += 1



def cat(n):
    while 1:
        time.sleep(random.randrange(10))
        if event.isSet():  #绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." % n)

if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t =threading.Thread(target=cat,args=(i,))
        t.start()

