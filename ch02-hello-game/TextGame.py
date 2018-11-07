# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/7 3:55 PM
# @Author: sunyf
# @File  : TextGame.py

"""" -- 第一个小游戏 -- """
temp = input("猜下你的幸运数字:\n")
guess = int(temp)
if guess == 8:
    print("你猜对啦")
    print("猜中了没有奖励")
else:
    print("你猜错啦")
print("游戏结束")
