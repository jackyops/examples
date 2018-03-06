#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/3/3 14:21'

from multiprocessing import Process,Queue,Pipe,Manager,Lock,Pool,freeze_support
import time
import os


# def f(name):
#     time.sleep(1)
#     print("hello jacky")
#
# if __name__ == "__main__":
#     for i in range(10):
#         p = Process(target=f,args=("jacky %s" %i,))
#         p.start()
#     # p.join()


# def f(q):
#     q.put([42,None,'hello'])
#
#
# if __name__ ==  "__main__":
#     q = Queue()
#     p = Process(target=f,args=(q,))
#     p.start()
#     print(q.get())
#     p.join()


# Pipe
# def f(conn):
#     conn.send([42,None,'hello from child'])
#     print("from parent:",conn.recv())
#     conn.close()
#
# if __name__ ==  "__main__":
#     parent_conn,child_conn = Pipe()
#     p = Process(target=f,args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())
#     parent_conn.send("hello jakcy main")
#     p.join()



# manager
# def f(d,l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.append(os.getpid())
#     print(l)
#
#
# if __name__ == "__main__":
#     with Manager() as manager:
#         d = manager.dict()           # 生成一个字典，可在多个进程间共享和传输
#         l = manager.list(range(5))   # 生成一个列表，可在多个进程间共享和传输
#         p_list = []
#         for i in range(5):
#             p = Process(target=f,args=(d,l))
#             p.start()
#             p_list.append(p)
#         for res in p_list:
#             res.join()
#         print(l)

# def f(l,i):
#     l.acquire()
#     try:
#         print('hello world',i)
#     finally:
#         l.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     for num in range(10):
#         p = Process(target=f,args=(lock,num))
#         p.start()


def Foo(i):
    time.sleep(1)
    print("in process",os.getpid())
    return i + 100


def Bar(arg):
    print('---> exec done:')


if __name__ == "__main__":
    #freeze_support()
    pool = Pool(5)
    for i in range(10):
        # apply同步执行（串行）  apply_async异步执行（并行）
        pool.apply_async(func=Foo,args=(i,),callback=Bar)
        # pool.apply(func=Foo,args=(i,))
        # pool.apply_async(func=Foo,args=(i,))

    print('end')
    pool.close()
    # 进程池中进程执行完毕后再关闭，如果注泽，那么程序直接关闭。.join()
    pool.join()

