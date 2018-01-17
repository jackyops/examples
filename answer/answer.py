#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/16 15:55'
import time,subprocess
from io import BytesIO
from PIL import Image
import requests
import random,os,json
from aip import AipOcr


config = {
    '头脑王者':{
        'title': (80,500,1000,880),
        'answers': (80,960,1000,1720),
        'point':[
            (240,1100,823,1220),
            (240,1290,823,1420),
            (240,1480,823,1610),
            (240,1670,823,1800),
        ]
    },
    '西瓜视频': {
        'box': (80,400,1000,1250)
    }
}

def get_screenshot():
    """获取截图"""
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    screenshot = process.stdout.read()
    screenshot = screenshot.replace(b'\r\n', b'\n')
    # with open('test.png', 'wb') as f:
    #     f.write(screenshot)

    # 调试图片
    # with open('test.png','rb') as f:
    #     screenshot = f.read()

    # 把图片存到内存
    img_fb = BytesIO()
    img_fb.write(screenshot)
    # 图片处理
    img = Image.open(img_fb)
    # 切出题目
    # title_img = img.crop((80,500,1000,880))
    title_img = img.crop((80,500,1000,880))
    # 切出答案
    # answers_img = img.crop((80, 960, 1000, 1720))
    answers_img = img.crop((80, 1080, 1000, 1880))
    # 拼接图片
    new_img = Image.new('RGBA',(920,1180))
    new_img.paste(title_img,(0,0,920,380))
    new_img.paste(answers_img,(0,380,920,1180))

    # 创建内存对象
    new_img_fb = BytesIO()
    new_img.save(new_img_fb,'png')
    with open('new_img.png','wb') as f:
        f.write(new_img_fb.getvalue())
    return new_img_fb


def get_word_by_img(img):
    APP_ID = "10702982"
    API_KEY = "OaHSSczkL6BB6MVwevR4h9I4"
    SECRET_KEY = "K1wFYdHRKxqLx0CXE9rpx66F5ttxGTGH "
    client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
    res = client.basicGeneral(img)
    return res


def baidu(question, answers):
    url = 'https://www.baidu.com/s'
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    data = {
        'wd':question
    }
    res = requests.get(url,params=data,headers=headers)
    res.encoding = 'utf-8'
    html = res.text

    # 分析
    for i in range(len(answers)):
        answers[i] = (html.count(answers[i]),answers[i],i)

    answers.sort(reverse=True)
    return answers

def click(point):
    cmd = 'adb shell input swipe %s %s %s %s %s' %(
        point[0],
        point[1],
        point[0] + random.randint(0,3),
        point[1] + random.randint(0,3),
        200
    )
    os.system(cmd)


def run():
    print('准备答题！')
    while True:
        input('请输入回车开始答题：')
        img = get_screenshot()
        info = get_word_by_img(img.getvalue())
        if info['words_result_num'] < 5:
            continue
        answers = [x['words'] for x in info['words_result'][-4:]]
        question = ''.join([x['words'] for x in info['words_result'][:-4]])
        res = baidu(question,answers)
        click(config['头脑王者']['point'][res[0][2]])
        
if __name__ == '__main__':
    run()
    #img = get_screenshot()
    #info = get_word_by_img(img.getvalue())
    #print(info)
   # print(json.dumps(info).decode("unicode-escape"))
   # print("打印info:%s", info)
