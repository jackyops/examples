# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/10/25 9:39'

import os,sys
import time
import threading

import requests
#http://api.hfsmrz.com/superapi/superapi/isConnect
url = ''

def get_idcard():
    try:
        r =requests.request('get','http://api.hfsmrz.com/superapi/super/auth/idcardp?condition=CfH%2FFCT7x9cQnDjbYf27yxQJvorFHZj4zV0eHkLYYtOJA4BRDEKKBGwaYaowI3lIPQLJXcXHmpqnaa81Me%2FHYS%2FJuXVRdYVo%2FQyKJ7H9OzYYNjfAWF8SfIelXRWUIRL2CtIqFjoqtMg19n53nn%2B2BDADV5MGbX%2FClkoj9Mh4SHa421%2FCPPTd3E6kV%2BFaoVlQ460MzSK3m%2FG8eaaXgdanH2VV9Ak4iXMuLal1ZGuu96LmFXDDjVGeRP%2FPlevFpxtxS7wsNGYLGOKFj%2BvMKcazY111ZbuD2cbFqMcfpFFRa9O1O9%2FHhPQjnAnyS3ftOKTS&userCode=HFJK20160729000004&signature=0rnEAq8jvuaN%2F77iThRfN%2BdmMqgmOWC1dg%2F8bDu%2BN%2Ffu%2Fx%2FWV%2FKWiXBf39CHpDxFNC2eTHQ%2B3ZzBV6lg4XWrWA%3D%3D&vector=12345678')
        #r =requests.request('get','http://api.hfsmrz.com/superapi/superapi/isConnect')
    except Exception as e:
        print(e)

    print("---------------------")
    print(r.headers)
    print(r.status_code)
    print(r.text)

#长连接版本
def get_link():
    #url = 'http://api.hfsmrz.com/superapi/superapi/isConnect'
    url = 'http://api.hfsmrz.com/superapi/super/auth/idcardp?condition=CfH%2FFCT7x9cQnDjbYf27yxQJvorFHZj4zV0eHkLYYtOJA4BRDEKKBGwaYaowI3lIPQLJXcXHmpqnaa81Me%2FHYS%2FJuXVRdYVo%2FQyKJ7H9OzYYNjfAWF8SfIelXRWUIRL2CtIqFjoqtMg19n53nn%2B2BDADV5MGbX%2FClkoj9Mh4SHa421%2FCPPTd3E6kV%2BFaoVlQ460MzSK3m%2FG8eaaXgdanH2VV9Ak4iXMuLal1ZGuu96LmFXDDjVGeRP%2FPlevFpxtxS7wsNGYLGOKFj%2BvMKcazY111ZbuD2cbFqMcfpFFRa9O1O9%2FHhPQjnAnyS3ftOKTS&userCode=HFJK20160729000004&signature=0rnEAq8jvuaN%2F77iThRfN%2BdmMqgmOWC1dg%2F8bDu%2BN%2Ffu%2Fx%2FWV%2FKWiXBf39CHpDxFNC2eTHQ%2B3ZzBV6lg4XWrWA%3D%3D&vector=12345678'
    client = requests.session()
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive'}
    r = client.get(url, headers=headers)
    print("---------------------")
    print(r.headers)
    print(r.status_code)
    print(r.text)



def nums(num):
    for i in range(num):
        get_idcard()


if __name__ == '__main__':
    for i in range(1):
        brnow = time.time()
        t = threading.Thread(target=get_link)
        #t.setDaemon(t)
        t.start()
        afternow = time.time()
        print(afternow - afternow)
