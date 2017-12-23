# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/20 21:12'

import requests
import re
import pymysql

conn = pymysql.connect(host='192.168.5.100',port=3306,user='jacky',passwd='123456',db='quansw',charset='utf8')
cursor = conn.cursor()

def getSortNovelList():
    response = requests.get('http://www.quanshuwang.com/list/1_1.html')
    response.encoding = 'gbk'
    result = response.text
    # print(result)
    reg = r'<a target="_blank" title="(.*?)" href="(.*?)"'
    novelurlList = re.findall(reg,result)
    return novelurlList

def getNovelInfo(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'<meta property="og:image" content="(.*?)"/>'
    imgUrl = re.findall(reg,result)[0]
    reg = r'<meta property="og:novel:category" content="(.*?)"/>'
    sort = re.findall(reg,result)[0]
    reg = r'<meta property="og:novel:author" content="(.*?)"/>'
    author = re.findall(reg,result)[0]
    reg = r'<meta property="og:novel:status" content="(.*?)"/>'
    status = re.findall(reg,result)[0]
    reg = r'<meta property="og:novel:latest_chapter_url" content="(.*?)"/>'
    chapterUrl = re.findall(reg,result)[0]
    return imgUrl,sort,author,status,chapterUrl


def getChapterList(url):
    response =requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'<li><a href="(.*?)" title="(.*?)</a></li>'
    chapterListurl = re.findall(reg,result)
    return chapterListurl

def getChapterContent(url):
    response =requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = 'style5\(\);</script>(.*?)<script type="text/javascript">style6'
    # re.S 表示匹配多行
    chapterContent = re.findall(reg,result,re.S)[0]
    return chapterContent

def main():
    for novelName,novelurl in getSortNovelList():
        imgUrl, sort, author, status, chapterUrl = getNovelInfo(novelurl)
        print(imgUrl, sort, author, status, chapterUrl)
        cursor.execute("insert into novel(sortname,name,imgurl,description,status,author) VALUES('{}','{}','{}','{}','{}','{}')".format(sort,novelName,imgUrl,'这是描述',status,author))
        conn.commit()
        lastrowid = cursor.lastrowid #刚插入数据ID值　
        for chapterUrl,chapterName in getChapterList(chapterUrl):
            chapterContent = getChapterContent(chapterUrl)
            cursor.execute("insert into chapter(noverid,title,content) VALUES ({},'{}','{}'))".format(lastrowid,chapterName,chapterContent))
            conn.commit()

getSortNovelList()



cursor.close()
conn.close()