#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/15 16:36'

import requests,base64

class RequestsElasticSearchClass(object):
    def __init__(self, host, port, user, passwrod):
        self.url = 'http://' + host + ':' + str(port)
        basicpwd = base64.b64encode((user + ':' + passwrod).encode('UTF-8'))
        self.headers = {"User-Agent": "shhnwangjian",
                        "Content-Type": "application/json",
                        "Authorization": "Basic {}".format(basicpwd.decode('utf-8'))}

    def search(self, indexname, size=10):
        gettdata = {"sort": "@timestamp:desc",
                    "size": size}
        url = self.url + '/' + indexname + '/_search'
        ret = requests.get(url, headers=self.headers, timeout=10, params=gettdata)
        print(ret.text)