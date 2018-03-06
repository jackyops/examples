#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/3/4 22:21'
import time

# 手动切换
# from greenlet import greenlet
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
# def test2():
#     print(13)
#     gr1.switch()
#     print(35)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# #
# gr1.switch()

# 自动切换
import gevent

def foo():
    print("Running in foo")
    gevent.sleep(2)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(2)
    print('Implicit context switch back to bar')
def func3():
    print("running fun3")
    gevent.sleep(0)
    print("running func3 again")

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(func3),
])
