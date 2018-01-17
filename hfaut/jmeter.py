# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/10/26 11:35'
'''
#http://blog.csdn.net/wuxiaobingandbob/article/details/38334211
'''
import threading,time,httplib2,random,requests

urls = [
    "/test?page=",
    "/test2?orderby=a&page=",
    "/test3?orderby=a&page=",
]

MAX_PAGE = 1000
SERVER_NAME = "api.hfsmrz.com"
TEST_COUNT = 1000

class RequestThread(threading.Thread):
    def __init__(self,thread_name):
        threading.Thread.__init__(self)
        self.test_count = 0

    def run(self):
        i = 0
        while i < TEST_COUNT:
            self.test_performace()
            i += 1

    def test_performace(self):
        for i in range(0,random.randint(0,100)):
            url =urls[random.randint[0,len(urls)-1]]
            url += str(random.randint(0,MAX_PAGE))
        print(url)

        try:
            rsps = requests.request('get',SERVER_NAME)
            if rsps.status_code == 200:
                data = rsps.text()
            self.test_count += 1
        except Exception as e:
            print(e)
        rsps.close()

if __name__ == "main":
    start_time = time.time()
    threads = []
    #并发的线程数
    thread_count = 100
    i = 0

    while i < thread_count:
        t = RequestThread("thread"+str(i))
        threads.append(t)
        t.start()
        i+=1

    # 接受统计的命令
    word = ""
    while True:
        word =input("cmd:")
        if word =="s":
            time_span = time.time()-start_time
            all_count = 0
            for t in threads:
                all_count += t.test_count
                print("%s Request/Second" %str(all_count/time_span))
        elif word == "e":
            TEST_COUNT = 0
            for t in threads:
                t.join(0)
        break



