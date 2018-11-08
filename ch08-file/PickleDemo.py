# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 4:23 PM
# @Author: sunyf
# @File  : PickleDemo.py

""" 泡菜模块 """

import pickle

"""---写入二进制文件---"""
l1 = [30, '孙', ['sun','yi','feng']]
p1 = open("data.pkl", mode='wb')
pickle.dump(l1, p1)
p1.close()

"""---读出二进制文件---"""
p2 = open("data.pkl", mode='rb')
l2 = pickle.load(p2)
print(l2)

