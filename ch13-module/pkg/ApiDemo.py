# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 4:48 PM
# @Author: sunyf
# @File  : ApiDemo.py

import timeit, sys

t = timeit.Timer()

print('---------------------sys.path：环境变量的搜索路径-----------------------------------')
print(sys.path)

print('---------------------dir(timeit)：模块所有的变量、函数、类---------------------------')
print(dir(timeit))

print('---------------------__all__：模块的接口,比如类、接口，不包括私有变量、方法-------------')
print(timeit.__all__)

print('---------------------__dict__：对象拥有的属性--------------------------------------')
print(t.__dict__)

print('---------------------__doc__：模块的简介-------------------------------------------')
print(timeit.__doc__)

print('---------------------help()：模块的帮助--------------------------------------------')
print(help(timeit))
