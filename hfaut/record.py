#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/1/30 13:48'

def strnum(num):
    if num < 10:
        return "0" + str(num)
    elif num >= 10:
        return str(num)
    else:
        return " "

def w_file(str):
    with open("log.txt",'rw') as f:
        f.write(str)


def c_logs(str,months):
    for d in range(1,32):
        for i in range(24):
            tmp = str + strnum(months) + strnum(d) + strnum(i)
            print(tmp)




def c_record():
    pass


if __name__ == '__main__':
    print(c_logs("t_merchant_data_query_record_",1))