# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 4:12 PM
# @Author: sunyf
# @File  : ModuleDemo.py

import os

""" os有很多处理文件路径的方法 """

v1 = os.getcwd();

print("---获取当前路径---")
print(os.getcwd())

print("---获取目录文件---")
print(os.listdir())

print("---执行系统命令---")
os.system("ls -al")