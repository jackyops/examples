#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/15 16:35'

"""
pip install elasticsearch
"""

from elasticsearch import Elasticsearch


class ElasticSearchClass(object):
    def __init__(self, host, port, user, passwrod):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwrod
        self.connect()

    def connect(self):
        self.es = Elasticsearch(hosts=[{'host': self.host, 'port': self.port}],
                                http_auth=(self.user, self.password))

    def count(self, indexname):
        """
        :param indexname:
        :return: 统计index总数
        """
        return self.es.count(index=indexname)

    def delete(self, indexname, doc_type, id):
        """
        :param indexname:
        :param doc_type:
        :param id:
        :return: 删除index中具体的一条
        """
        self.es.delete(index=indexname, doc_type=doc_type, id=id)

    def get(self, indexname, id):
        return self.es.get(index=indexname, id=id)

    def search(self, indexname, size=10):
        try:
            return self.es.search(index=indexname, size=size, sort="@timestamp:desc")
        except Exception as err:
            print(err)


