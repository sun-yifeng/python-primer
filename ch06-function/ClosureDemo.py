# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 9:51 AM
# @Author: sunyf
# @File  : ClosureDemo.py

"""
什么是闭包：
1、函数中嵌套函数,把函数当做一个变量声明，看起来是函数将变量包裹起来，所有叫做闭包；
2、如果将闭包函数返回，外包调用引用了闭包函数，容易造成循环引用；
3、修改闭包中的局部变量用nonlocal,修改全局变量用global
"""

def fun1():
    x = 5
    def fun2():
        #修改闭包中的局部变量
        nonlocal x
        x *= x
        return x
    #fun1的返回结果
    return fun2

v1 = fun1()()
print(v1)