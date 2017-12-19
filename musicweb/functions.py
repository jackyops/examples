# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/19 21:44'

# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/17 21:12'

import requests
import re
import json

def get_mp3_by_sid(sid):
    # 根据sid 获取歌曲MP3的地址
    api = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17207370277060591794_1513517218562&songid=%s&_=1513517220200' % sid

    response = requests.get(api)
    data = response.text
    data = re.findall(r'\((.*)\)',data)[0]
    data = json.loads(data)


    #取得歌曲名称
    mp3_name = data['songinfo']['title']
    print("歌曲名：%s" % mp3_name)
    #  取得歌曲mp3的下载地址
    mp3_url = data['bitrate']['file_link']

    #发送http请求
    response = requests.get(mp3_url)
   # print(response.content)  # 是二进制数据

    # 持久化 写文件
    filename = '%s.mp3' % mp3_name
    with open(filename,'wb') as f:
        f.write(response.content)

def get_sids_by_name(query):
    #根据查询的内容获取sid
    # http://music.baidu.com/search?key=%E5%BC%A0%E5%AE%87
    api = 'http://music.baidu.com/search'
    data = {
        'key':query
    }

    respone = requests.get(api,params=data)
    html = respone.text
    sids = re.findall(r'sid&quot;:(\d+),',html)
    return sids

def get_music_info_by_name():
    pass
