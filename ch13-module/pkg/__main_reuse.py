# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/11 3:10 PM
# @Author: sunyf
# @File  : __main_reuse.py

import __main_module as tc

"""  """
print(__name__)
print(tc.__name__)

print("32摄氏度 = %.2f华氏度" % tc.c2f(0))
print("99华氏度 = %.2f摄氏度" % tc.f2c(0))