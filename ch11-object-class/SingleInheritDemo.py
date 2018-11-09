# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 10:19 AM
# @Author: sunyf
# @File  : SingleInheritDemo.py

import random as r

""" 定义一个父类 """
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x = -1
        print("我的位置是：", self.x, self.y)

""" 定义如下子类 """
class GoldFish(Fish):
    pass

class GarpFish(Fish):
    pass

class SalmFish(Fish):
    pass

"""  覆盖子类  """
class SharkFish(Fish):
    def __init__(self):
        # 注意这里要调用父类的super函数
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃饭")
            self.hungry = False
        else:
            print("太饱了")

""" 创建对象 """
fish = Fish()
fish.move()

goldFish = GoldFish()
goldFish.move()

sharkFish = SharkFish()
sharkFish.move()


