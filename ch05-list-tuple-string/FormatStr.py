# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 1:31 AM
# @Author: sunyf
# @File  : FormatStr.py

""" 格式化字符串 """

print("-----字符串的占位符用法-----")
f1 = "{0} love {1}.{2}".format("I", "sun", "yifeng")
print(f1)
f2 = "{a} love {b}.{c}".format(a="you", b="fan", c="bingbing")
print(f2)
f3 = "{0}:{1:2f}".format("圆周率", 3.14159)
print(f3)

print("-----字符串的百分号用法-----")
s1 = '%c' % 97
print(s1)
s2 = '%c%c%c%c%c'%(70, 105, 115, 104, 67)
print(s2)



