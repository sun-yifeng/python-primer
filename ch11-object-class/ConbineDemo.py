# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 10:53 AM
# @Author: sunyf
# @File  : ConbineDemo.py

""" 组合代替多重继承 """

class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池里有乌龟%d只,小鱼%d只!" % (self.turtle.num, self.fish.num))

""" 验证组合代替继承 """
pool = Pool(1, 10)
pool.print_num()
