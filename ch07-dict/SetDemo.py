# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 2:09 PM
# @Author: sunyf
# @File  : SetDemo.py

"""  集合（SET） """

print("---集合没有重复的数据1---")
set1 = {1, 2, 3, 4, 5, 6, 1, 2 ,3, 5}
print(set1)

print("---集合没有重复的数据2---")
set2 = set([1, 2, 3, 4, 5, 1, 2, 3, 3, 5, 7])
print(set2)

print("---遍历集合---")
for each in set1:
    print(each, end='|')

print("---不可变集合---")
set3 = frozenset(['sun', 'yi', 'feng'])
print(set3)

