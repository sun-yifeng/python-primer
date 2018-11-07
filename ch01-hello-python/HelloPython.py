# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/7 3:55 PM
# @Author: sunyf
# @File  : TextGame.py
# 窗口输入姓名

name = input("Please input your name:")
# 打印三种方法
print("hello {0}".format(name))
print("hello " + name)
print("hello %s" %name)

# 不加括号是2.x的语法
# print "hello"

print("I love python\n" *10)