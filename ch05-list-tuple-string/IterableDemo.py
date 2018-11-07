# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 1:48 AM
# @Author: sunyf
# @File  : IterableDemo.py

""" list  """
l1 = list("sunyf")
print(l1)
print(max(l1))
print(min(l1))
print(len(l1))

print("-----集合相加-----")
l2 = [1, 2, 3, 4, 5, 6]
print(sum(l2))

print("-----二元组：元素的数量为二-----")
s1 = "Sunyf"
for each in enumerate(s1):
    print(each)

print("-----zip：返回两个集合组成的二元组-----")
z1 = [1, 2, 3, 4, 5, 6]
z2 = "sunyi"
for each in zip(z1, z2):
    print(each)

