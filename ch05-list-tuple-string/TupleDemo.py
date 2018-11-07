# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/7 6:49 PM
# @Author: sunyf
# @File  : TupleDemo.py

"""  元组是不可以修改的列表  """

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple1)
# 一个元素的元组请用逗号
tuple2 = 8 * (8)
tuple3 = 8 * (8,)
print(tuple2)
# tuple2是整数类型
print(type(tuple2))
print(tuple3)
# tuple2是元组类型
print(type(tuple3))

""""  元组不能修改但是能覆盖  """
tuple1 = tuple1[2:3]+('伪造一个新的元组覆盖原来的元组',)+tuple1[4:7]
print(tuple1)