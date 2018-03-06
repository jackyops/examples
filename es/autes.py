#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/26 17:10'

from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean,analyzer, InnerObjectWrapper, Completion, Keyword, Text, Integer
from elasticsearch_dsl.connections import connections

#创建服务器链接,非常终于
connections.create_connection(hosts=["localhost"])

#定义数据类，继承DocType,定义各个字段数据类型，在from elasticsearch_dsl import中导入需要的数据类型，包括字符串，整型，布尔等等
class LagouType(DocType):
    # id = Text(analyzer="ik_max_word")
    # created = Integer()
    # resTime = None
    status = None
    recordStatus = Text()
    createTime = datetime.now()
    # updateTime = None
    # operatorId = None
    # remark = None
    # batchNo = None
    # channelCode = None
    # userCode = Text()
    # apiCode = Text()
    # appCode = Text()
    # queryObjCode = Integer
    # queryReason = Text()
    # cacheType = Integer
    # merTradeNo = Integer
    # platTradeNo = Text()
    # objwayTradeNo  = Text()
    # queryResult = Integer
    # resultDesc= Text()
    # queryCondition = Text()
    # objwayResMsg = Text()
    # platResMsg = Text()
    # queryTime = Integer()
    # elapsedTime = Integer()
    # unitPrice = Integer()
    # temp1 = None
    # temp2 = None
    # temp3 = None
    # temp4 = None
    # temp5 = None

    #建立链接的index和doc，在类中建立类，必须是Meta类，用于传入index值和type（表）值
    class Meta:
        index = "jacky_index"
        doc_type = "job"

class Elasticsearch_pipeline(object):
    def __init__(self):
        pass
    def process_item(self,item,spider):
        lagou = LagouType()
        lagou.status = item['status']
        lagou.recordStatus = item['recordStatus']
        lagou.createTime = item['createTime']
        lagou.save()

        return item




#pipeline调用
class Elasticsearch_pipeline(object):
    def __init__(self):
        pass

    #在process_item中调用item的方法（item.save_to_elasticsearch()）
    def process_item(self,item,spider):
        item.save_to_elasticsearch()
        return item

#settings中开启item_pipeline

    ITEM_PIPELINES = {
    'lagou_spider.pipelines.Elasticsearch_pipeline': 1
    }

#settings中开启item_pipeline

    ITEM_PIPELINES = {
    'lagou_spider.pipelines.Elasticsearch_pipeline': 1
    }







class Elasticsearch_Option:
    def __init__(self):
        pass

#注意点1：注意大小写，进行分词分析时，elasticsearch的分词器会把自动把所有词变成小写


#match 用法，对 match 传入的值进行分词，符合分词结果的都可以检索到
def match_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
           "query": {
                "match": {
                    'title':'C++后端工程师'
                }
            }
        }
    )

#term 用法，不对 term  传入的值进行分词
def term_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
           "query": {
                "term": {
                    'salary_min':'2000000'
                }
            }
        }
    )

#terms 用法，可传入列表，符合列表内的值都可以检索到
def terms_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
            "query": {
                "terms": {
                    'title': ['python','java','c++']  #千万注意大小写
                }
            }
        }
    )

#from 和 size 的用法
def from_size_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
           "query": {
                "match": {
                    'title':'工程师'
                }
            },
            "from":0,
            "size":4
        }
    )

#match_all操作
def match_all_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
           "query": {
                "match_all": {
            }
           }
        }
    )

# match_phrase 短语查询
def match_phrase_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
            "query": {
                "match_phrase": {
                    "title": 'python研发工程师'
                }
            }
        }
    )
    for i in response['hits']['hits']:
        print(i['_source'])


#multi_match查询，单一查询条件查询多列（fields）
def multi_match_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
            "query": {
                "multi_match": {
                    "query":"深圳",
                    "fields": ['title','city']    #查询 fields 多个字段中，只要有：query查询内容的关键字的就查询出来。
                }
            }
        }
    )
    #仔细留意response返回结构
    for i in response['hits']['hits']:
        print(i['_source'])

#排序操作
def sort_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
            "query": {
            "match_all":{}
            },
            "sort":{
                "comment":{         #sort下面先制定需要排序的栏
                    "order": "asc"
                }
            }
        }
    )
    # 仔细留意response返回结构
    for i in response['hits']['hits']:
        print(i['_source'])

#范围查询，gte：大于等于； gt：大于； lte：小于等于； lt：小于； boots：表示权重
def range_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
            "query": {
                "range":{
                    "comment":{     #range下面是要确定范围的field
                        "gt": 15,
                        "lt": 20
                    }
                }
            }
        }
    )
    # 仔细留意response返回结构
    for i in response['hits']['hits']:
        print(i['_source'])

#wildcard,模糊查询
def wildcard_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
            "query": {
                "wildcard":{
                    "title":{     #range下面是要确定范围的field
                    "value":"pyth*n"    # "*" 标识通配
                    }
                }
            }
        }
    )
    # 仔细留意response返回结构
    for i in response['hits']['hits']:
        print(i['_source'])


# bool查询
# filter：字段过滤并且不参与打分，过滤掉非数组内的内容
# must：满足数组中所有的条件，“与”
# should：数组中的查询条件满足一个或多个，“或”
# must_not：数组中的查询条件一个都不能去满足，“非”

def bool_option(self):
    client = Elasticsearch()
    response = client.search(
        index="lagou",
        body={
              "query": {
                "bool": {
                  "must": [{
                    "match_all":{}
                  }],
                  "filter": {
                    "term": {
                      "title": '工程师'
                    }
                  },
                  "must_not": [{
                    "match": {
                      "comment": 16
                    }
                  }],
                  "should": [{
                    "match": {
                      "title": 'c'
                    }
                  }]
                }
              }
            }
    )
    # 仔细留意response返回结构
    for i in response['hits']['hits']:
        print(i['_source'])







if __name__ == "__main__":
    #调用init()方法建立映射（mappings）
    LagouType.init()



