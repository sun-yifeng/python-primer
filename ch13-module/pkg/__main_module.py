# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 4:27 PM
# @Author: sunyf
# @File  : __main_module.py

""" 温度转换 """

def c2f(cel):
    fah = cel * 1.8 + 32
    return fah

def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

def test():
    print("测试，0摄氏度 = %.2f华氏度" % c2f(0))
    print("测试，0华氏度 = %.2f摄氏度" % f2c(0))

"""
注意：作为程序运行、作为模块调用，__name__的值不一样
"""
print("属性__name__的值为：" + __name__)

# 作为程序运行时，才调用test()方法，
if __name__ == '__main__':
   test()

