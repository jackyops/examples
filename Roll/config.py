# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/23 21:52'

import configparser
import random

target = configparser.ConfigParser()

target.read(r'E:\zyc\Projects\examples\examples\Roll\sgg.ini',encoding='utf8')
print(target['我的弹幕'][str(random.randint(1,5))])