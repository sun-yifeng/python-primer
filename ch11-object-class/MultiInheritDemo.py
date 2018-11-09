# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 10:45 AM
# @Author: sunyf
# @File  : MultiInheritDrremo.py

""" 多继承 """
class Base1:
    def foo1(self):
        print("我是foo1")

class Base2():
    def foo2(self):
        print("我是foo2")

class C(Base1, Base2):
    pass

c = C()
c.foo1()
c.foo2()