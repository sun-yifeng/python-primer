# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/7 5:41 PM
# @Author: sunyf
# @File  : ControlStatement.py

""" for循环  """
favorite = "fish C"
#遍历字符
for each in favorite:
    print(each, end=",")

""" range() """
#不会打印10，第三个参数是步长
for i in range(1, 10 ,1):
    print(i)

# break    无特殊之处
# continue 无特殊之处