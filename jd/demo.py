# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/23 22:12'

import time
from  multiprocessing.dummy import Pool as ThreadPool

#线程池
def print_hello(name):
    print('Hello',name)
    time.sleep(2)

name_list = ['jacky','steven','tom','jacky']
start_time = time.time()
pool = ThreadPool(4)
pool.map(print_hello,name_list)
pool.close()
pool.join()  #主线程等待子线程结束
end_time = time.time()

print('%d second' %(end_time - start_time))

#京东手机数据 js
