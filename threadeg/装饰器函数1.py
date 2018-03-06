#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/2/27 21:27'
import time

def outwarp(func):
    def warp(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        print("耗时长:%s" %(time.time() - start_time))
    return warp


@outwarp  # test1=warp(func)
def test1():
    time.sleep(2)
    print("this is test1")

@outwarp  # test2=outwarp()
def test2(name):
    time.sleep(1)
    print("this is test2: %s" % name)

test2("jacky")
test1()