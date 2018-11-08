# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 8:03 PM
# @Author: sunyf
# @File  : WithDemo.py

""" with语句省略了文件的关闭 """
try:
    with open("data.txt", mode='r', encoding='utf-8') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print("打开文件出错了：" + str(reason))

