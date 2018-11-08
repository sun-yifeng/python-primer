# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 1:49 PM
# @Author: sunyf
# @File  : DictMethod.py

""" 字典内置的方法 """

print("---创建一个字典---")
dict1 = {}
v2 = dict1.fromkeys((1, 2, 3))
print(v2)
v3 = dict1.fromkeys((1, 2, 3), "sunyf")
print(v3)
v4 = dict1.fromkeys((1, 2, 3), ("sunyf","zhangsan"))
print(v4)
print("---打印所有的key---")
print(v4.keys())
print("---打印所有的value---")
print(v4.values())
print("---打印所有的建值---")
print(v4.items())
print("---建是否存在（不存在会报错）---")
print(v4[1])
#print(v4[9])
print("---建是否存在（不存在不报错）---")
v5 = v4.get(9, "没有则添加")
print(v5)
print("---清空字典---")
v4.clear()
print(v4)


