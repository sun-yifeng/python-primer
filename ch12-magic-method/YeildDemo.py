# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 1:51 PM
# @Author: sunyf
# @File  : YeildDemo.py

""" 此栗子验收yeild 和 for循环的组合使用方法 """

"""
简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
于是函数继续执行，直到再次遇到 yield。
"""

"""
斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意数都可由前两个数相加得到，比如：
1 1 2 3 5
"""

""" 定义fibonacci函数 """
def fab(max):
    #注意此种赋值方法
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        #print(b)
        # 注意此种赋值方法
        a, b = b, a + b
        n = n + 1

""" 打印fibonacci数列 """
for i in fab(10):
    print(i)


