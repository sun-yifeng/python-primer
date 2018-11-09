# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 12:40 PM
# @Author: sunyf
# @File  : PerpertyDemo.py

class C:
    def __int__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)

c = C()
c.x = 12
print(c.x)
print(c.size5)
