#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/2/23 20:13'

import threading,time

# 使用类方法
# class MyThread(threading.Thread):
#     def __init__(self,n):
#         super(MyThread,self).__init__()
#         self.n = n
#
#     def run(self):
#         print("runnint task",self.n)
#
# t1 = MyThread("t1")
# t2 = MyThread("t2")
# t1.start()
# t2.start()

def run(n):
    print("task",n)
    time.sleep(2)
    print("task done %s" %n,threading.current_thread(),threading.active_count())

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i,))
    t.setDaemon(True)  # 把当前线程设置为守护线程，主线程退出所有的子线程都退出
    t.start()
    t_objs.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

# for t in t_objs:   # 揗环线程实例列表，等待所有线程执行完毕
#     t.join()

print("----all thread done ------",threading.current_thread(),threading.active_count())
print("cost:",time.time() - start_time)