# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/7 5:57 PM
# @Author: sunyf
# @File  : ListDemo.py

""" 列表（数组） """
number = [1, 2, 3, 4, 5]
#添加元素
number.append(6)
print(number)
#添加元素
number.extend([7, 8])
print(number)
#插入元素
number.insert(1, 0)
print(number)
#获取元素
print(number[0])
#删除元素
number.remove(1)
print(number)
del number[1]
print(number)
#del number
print(number)
#弹出元素
print(number.pop())
print(number.pop(3))