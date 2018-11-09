# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 5:17 PM
# @Author: sunyf
# @File  : Spider1.py

import urllib.request

res = urllib.request.urlopen("http://wwww.baidu.com")
html = res.read()
html = html.decode("utf-8")
print(html)
