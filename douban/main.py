#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2017/12/30 20:57'

import requests,re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}

def login():
    response = requests.get('https://accounts.douban.com/login')
    result = response.text
    reg = r'<img id="captcha_image" src="(.*?)"'
    codeImgUrl = re.findall(reg,result)[0]
    reg = r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
    captcha_id = re.findall(reg,result)[0]
    response = requests.get(codeImgUrl,headers=headers)
    codeImg = response.content
    fn = open('code.png','wb')
    fn.write(codeImg)
    fn.close()
    data = {
        'source': 'index_nav',
        'form_email': 'jackyzhousales@163.com',
        'form_password': 'jacky0829',
        'captcha-solution': input('请输入验证码:'),
        'captcha-id': captcha_id,
    }
    response = requests.post('https://www.douban.com/accounts/login',data=data,headers=headers)
    if 'Jacky' in response.text:
        print('登录成功')
    else:
        print('登录失败,正在重新登录')
        login()
        return

def comment(mid):
    data = {
        'ck':'Ur00',
        'interest':'wish',
        'rating':'',
        'foldcollect':'U',
        'tags':	'',
        'comment':'没看过,有看过的,推荐下'
    }
    response = requests.post('https://movie.douban.com/j/subject/{}/interest'.format(mid), data=data, headers=headers)
    print(response.text)



def getMoieId():
    response = requests.get('https://movie.douban.com/ithil_j/activity/movie_annual2017/widget/7', headers=headers)
    result = response.json()
    return result['res']['subjects']

login()
for i in getMoieId():
    print('https://movie.douban.com/subject/{}/'.format(i['id']))
    comment(i['id'])
