# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 2:24 PM
# @Author: sunyf
# @File  : FileDemo.py

""" 读取文件一定要加字符编码 """

f = open("data.txt", mode="r", encoding='UTF-8')

print("-----读取全部内容-----")
f.seek(0)
print(f.read())

print("-----读取一行内容-----")
f.seek(0)
print(f.readline())

print("-----读取全部内容-----")
f.seek(0)
print(list(f))

""" 写人文件一定要用参数w(覆盖模式),a(追加模式) """
f1 = open("data.txt", mode="a", encoding='UTF-8')
f1.write("我很好！\n" *3)
f1.close()

