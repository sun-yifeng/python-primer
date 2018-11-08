# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 6:19 PM
# @Author: sunyf
# @File  : TryExcept.py

"""  try exception 捕捉多个异常  """

print("--- 多个异常分别处理 ---")
try:
    int('abc')
    sum = 1 + 'a'
    f = open('data.txt', mode='r')
    print(f.read())
    f.close()
except OSError as reason:
    print("打开文件出错，错误原因：" + str(reason))
except TypeError as reason:
    print("文件类型出错，出错原因：" + str(reason))
except ValueError as reason:
    print("类型转换异常，错误原因：" + str(reason))
finally:
    f.close()


print("--- 多个异常一起处理 ---")
try:
    int('abc')
    sum = 1 + 'a'
    f = open('data.txt', mode='r')
    print(f.read())
    f.close()
except (OSError, TypeError, ValueError) as reason:
    print("错误原因：" + str(reason))











