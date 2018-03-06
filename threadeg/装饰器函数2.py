#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/2/27 21:27'

import time

user,passwd='jacky','123'
def auth(auth_type):
    print("auth_type:",auth_type)
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            username = input("Username:").strip()
            password = input("Password:").strip()

            if user == username and passwd == password:
                print("\033[32; 1mUser has passwd authnitaionc \033[0m")
                res = func(*args, **kwargs)
                print("----after authenticaion")
                return res
            else:
                print("\033[31; 1mInvalid username or passowd \033[0m")
        return wrapper
    return outwrapper




def index():
    print("welcome to index page")

@auth(auth_type="local")
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ladp")
def bbs():
    print("welcome to bbs page")

index()
print(home())
# bbs()