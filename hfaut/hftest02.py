# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/10/26 11:35'

import threading,time,random,requests

urls = [
    # "http://api.hfsmrz.com/superapi/superapi/isConnect",
    # "http://api.hfsmrz.com/superapi/superapi/isConnect",
    # "http://api.hfsmrz.com/superapi/superapi/isConnect",
    "http://api.zkteco.com/admin/a.html",
    "http://api.zkteco.com/admin/a.html",
    "http://api.zkteco.com/admin/a.html",
]

MAX_PAGE = 10
TEST_COUNT = 10

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
        url = urls[0]
        for i in range(0,random.randint(0,100)):
            url =urls[random.randint(0,len(urls)-1)]
            #print(url)

        try:
            rsps = requests.session()
            headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive'}
            r = rsps.request('get',url,headers=headers)
            if r.status_code == 200 and  r.text != '':
                data = r.text
                self.test_count += 1
                print("返回200状态%s次" % self.test_count)
            #rsps.close()
        except Exception as e:
           print(e)
           #rsps.close()

    def test(self):
        for i in range(0,random.randint(0,3)):
            url =urls[random.randint(0,len(urls)-1)]
            print(url)


if  __name__ == "__main__":
    start_time = time.time()
    threads = []
    #并发的线程数
    thread_count = 2
    i = 0

    while i < thread_count:
        t = RequestThread("thread"+str(i))
        threads.append(t)
        #time.sleep(0.3)
        t.start()
        i+=1

    for t in threads:
        t.join()

    #接受统计的命令
    # word = ""
    # while True:
    #     word =input("请输入:")
    #     if word =="s":
    #         time_span = time.time()-start_time
    #         all_count = 0
    #         for t in threads:
    #             all_count += t.test_count
    #             print("%s Request/Second" %str(all_count/time_span))
    #     elif word == "e":
    #         TEST_COUNT = 0
    #         for t in threads:
    #             t.join(0)
    #     break