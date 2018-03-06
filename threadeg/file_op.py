#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/3/1 22:06'

# r+ 读写
# w+ 写读  是先创建文件

f = open("txt",'w+',encoding="utf-8")
# for i in range(5):
#     print(f.readline())


# for index,line in enumerate(f.readlines()):
#     if index == 2:
#         print("-------")
#         continue
#     print(line.strip())
#
# for line in f:
#     print(line.strip())

# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.seek(0))
# print(f.readline(2))

# import sys,time
#
# for i in range(50):
#     sys.stdout.write("#")
#     sys.stdout.flush()
#     time.sleep(0.2)

print(f.readline())
print(f.readline())
print(f.readline())
f.write("\n======================")
print((f.readline()))