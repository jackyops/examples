#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/11 21:07'
from PIL import Image
import os,sys,time,random,json,re,subprocess

def get_screen_size():
    # 获取手机分辨率
    # 1920*1080
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print("请安装adb及驱动并配置环境变量")
        exit()
    m = re.search(r'(\d+)x(\d+)',size_str)
    if m:
        return "%sx%s" % (m.group(2),m.group(1))



def init():
    """初始化，获取配置，检查环境"""
    # 获取分辨率
    screen_size = get_screen_size()
    # 配置文件路径
    config_file_path = 'config/%s/config.json' % screen_size
    if os.path.exists(config_file_path):
        with open(config_file_path,'r') as f:
            print("Load config file %s" % config_file_path)
            return json.loads(f.read())
    else:
        with open('config/default.json','r') as f:
            print("Load config file %s" % config_file_path)
            return json.loads(f.read())

def find_piece_board(img,config):
    """ 根据图片和配置文件找到棋盘棋子的坐标"""
    # 获取图片宽和高
    w,h = img.size
    # 扫描启始坐标
    scan_stary_y = 0
    # 图片的像素矩阵
    img_pixel = img.load()
    for i in range(h//3,h*2//3,50):
        first_pixel = img_pixel[0,i]
        for j in range(1,w):
            pixel = img_pixel[j,i]
            # 如果不是纯色的，跳出，说明找到Y轴的最大值
            if first_pixel[:-1] != pixel[:-1]:
                scan_stary_y = i - 50
                break
        if scan_stary_y:
            break
    # 开始扫描棋子
    left = 0
    right = 0
    for i in range(scan_stary_y,h*2//3):
        flag = True
        # 切掉左右1/8
        for j in range(w//8,w*7//8):
            pixel = img_pixel[j,i]
            # 根据棋子
            if ( 50 < pixel[0] < 60) and (53 < pixel[1] < 63) and (95 < pixel[2] < 110):
                if flag:
                    left = j
                    flag = False
                right = j
                piece_y_max = max(i,piece_y_max)
    piece_x = (left+right)//2
    piece_y = piece_y_max - config['piece_base_height_1_2']






def get_screenshot():
    """ 获取手机截图 auto.png"""
    process = os.system('adb shell screencap -p', shell=True,stdout=subprocess.PIPE)#获取当前界面的手机截图
    screenshot = process.stdout.read()
    screenshot = screenshot.replace(b'\r\r\n',b'\n')
    with open('auto.png','wb') as f:
        f.write(screenshot)



def jump(distance,param):
    """ 跳一跳"""


def run():
    config = init()
    while True:
        get_screenshot()
        # 生成图片对象
        img = Image.open('auto.png')
        # 获取棋子，棋盘坐标
        piece_x,piece_y,board_x,board_y = find_piece_board(img,config)
        # 计算距离
        distance = ((piece_x-board_x)**2 + (piece_y - board_y)**2)**0.5
        # 开跳
        jump(distance,config['press_ratio'])
        # 增加随机时间，防人跳
        time.sleep(1 + random.random() * 2)

if __name__ == '__main__':
    #run()
    print(get_screen_size())