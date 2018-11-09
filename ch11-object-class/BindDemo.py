# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 11:10 AM
# @Author: sunyf
# @File  : BindDemo.py

"""方法必须有实例才能被调用，这种限制就是绑定！"""
class A:
    def printA(self):
        print("python严格要求：方法必须有实例才能被调用，这种限制就是绑定！")
a = A()
a.printA()

"""  """
class B:
    def setX(self, x, y):
        self.x = x
        self.y = y
    def setY(self):
        print(self.x, self.y)
b = B()
print("---打印对象的属性---")
print(b.__dict__)

print("---打印类的属性---")
print(B.__dict__)

b.setX(4, 5)

print("---再次打印对象的属性---")
print(b.__dict__)

print("---再次打印类的属性---")
print(B.__dict__)
