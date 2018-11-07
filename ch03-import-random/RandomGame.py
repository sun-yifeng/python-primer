# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/7 4:50 PM
# @Author: sunyf
# @File  : RandomGame.py

"""" -- 猜数字的游戏 -- """
import random

secret = random.randint(1, 10)
temp = input("猜下你的幸运数字:\n")
guess = int(temp)

while guess != secret:
    if guess == secret:
        print("你猜对啦！")
    else:
        if guess > secret:
            print("你猜的数字太大！")
        else:
            print("你猜的数字太小！")

    temp = input("请重新输入你的幸运数字:\n")
    guess = int(temp)

print("游戏结束！")
