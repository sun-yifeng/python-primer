# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 10:52 AM
# @Author: sunyf
# @File  : RecursionDemo.py

"""  递归函数 """
def myRecesion(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
v = myRecesion(5)
print(v)
