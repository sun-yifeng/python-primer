# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 10:32 AM
# @Author: sunyf
# @File  : LambdaDemo.py

"""
1、lambda表达式就是匿名函数
2、冒号的左边是参数，后边是表达式
3、只执行一次的函数，不需要定义函数名
"""

print("-----lambda函数的定义-----")
g = lambda x, y: x + y
print(g(3,4))

print("-----filter函数的使用-----")
l1 = filter(lambda x:x%2, range(10))
#filter返回迭代器类型
print(list(l1))

print("-----map函数的使用-----")
l2 = map(lambda x:x/2, range(10))
#filter返回迭代器类型
print(list(l2))

