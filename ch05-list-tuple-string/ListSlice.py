# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/7 6:08 PM
# @Author: sunyf
# @File  : ListSlice.py

""" 数组分片 """

print("数组分片")
list = [1, 2, 3, 4, 5, 6, 7]
print(list[0:3])
print(list[:3])
print(list[4:])
print(list[0:9:2])
print(list[::-1])

""" 数组相加 """
print("---数组相加---")
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 + list2)

""" 重复操作符 """
print("---重复的操作符---")
list1 *= 5
print(list1)

#数组的方法
print("---数组内置方法---")
print(dir(list1))



