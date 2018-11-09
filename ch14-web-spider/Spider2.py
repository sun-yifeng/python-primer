# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 5:44 PM
# @Author: sunyf
# @File  : Spider2.py

import urllib.request

res = urllib.request.urlopen("https://www.baidu.com/img/bd_logo1.png")
img = res.read()

with open('bd_logo1.png', 'wb',) as f:
    f.write(img)
