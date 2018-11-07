# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/7 5:08 PM
# @Author: sunyf
# @File  : TypeConvert.py

"""  数据类型转换 """

#字符转为数字
a = '520'
b = int(a)
print(b)

#浮点数转整数
c = 5.99
d = int(c)
print(d)

#字符转浮点数
v1 = '520'
v2 = float(v1)
print(v2)

#数字转为字符
v1 = '5.99'
v2 = str(v1)
print(v2)

#
t = type(v2)
print(t)