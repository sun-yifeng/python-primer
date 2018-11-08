# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 11:01 PM
# @Author: sunyf
# @File  : Gui.py

import sys
import easygui as g

#弹出对话框
g.msgbox("我们开始一个小游戏！")
#弹出对话框
choice = ["谈恋爱", "写程序" , "琴棋书画"]
choice = g.choicebox("你学到什么知识？", "一个小游戏", choice)
g.choicebox("你选择的是：" + str(choice), "结果")
msg = "你希望重新开始小游戏吗"
title = "请选择"
if g.ccbox(msg, title): #
    pass
else:
    sys.exit(0)


