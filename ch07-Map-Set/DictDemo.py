# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 1:18 PM
# @Author: sunyf
# @File  : DictDemo.py

"""  字典（键值对）  """

print("字典的声明方法1")
dict1 = {}
dict1 = dict({})

print("字典的声明方法2")
dict2 = dict((('a', 10), ('b', 20), ('c', 30)))
print(dict2)

print("字典的声明方法3")
dict3 = dict(A=1, B=2, C=3, D=4)
print(dict3)

print("字典的声明方法3")
dict3['E'] = 5
print(dict3)

print("字典的声明方法4")
dict4 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(dict4)

print("字典的声明方法5")
dict5 = dict([('X', 'x'), ('Y', 'y'), ('Z', 'z')])
print(dict5)





