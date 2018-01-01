#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/1 15:44'

import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.5.100', port=3306, user='jacky', passwd='123456', db='quansw')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from chapter")
# print(cursor.fetchone())
# print(cursor.fetchall())

data = [
    (1,"tom","tom is txt"),
    (2,"jack","tom is txt"),
    (3,"Lucy","tom is txt"),
    (4,"steven","tom is txt"),
]

cursor.executemany("insert into chapter (noverid,title,content) VALUES (%s,%s,%s)",data)


# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])


# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()