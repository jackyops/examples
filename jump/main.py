#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/6 14:26'

import os,time
import PIL,numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

need_update = True

def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png')#获取当前界面的手机截图
    os.system('adb pull /sdcard/screen.png')#下载当前这个截图到当前电脑当前文件夹下
    return numpy.array(PIL.Image.open('screen.png'))

# 计算炫的长度
def jump_to_next(point1, point2):
    x1, y1 = point1; x2, y2 = point2
    # swipe x1 y1 x2 y2 time  按下x1坐标 按下y1坐标 抬上x2坐标，抬上y2坐标,time按压的时间 一个像素点大概要乘以1.35
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance*1.35)))




# 绑定的鼠标单击事件
def on_calck(event,coor=[]):
    global need_update
    coor.append((event.xdata,event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(),coor.pop())
        need_update = True

#更新图片 重画图片
def update_screen(frame):
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,




figure = plt.figure()#创建一个空白的图片对象/创建一张图片

# 把获取的图片画在坐标轴上面,animated 表示？
axes_image = plt.imshow(get_screen_image(), animated=True)
# 单击回调函数调用
figure.canvas.mpl_connect('button_press_event', on_calck)
ani = FuncAnimation(figure, update_screen, interval=50, blit=True)
plt.show()