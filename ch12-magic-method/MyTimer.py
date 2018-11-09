# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 12:07 PM
# @Author: sunyf
# @File  : MyTimer.py

import time as t

class MyTimer:
    def start(self):
        self.start = t.localtime()
        print("计时开始")
    def stop(self):
        self.stop = t.localtime()
        print("即时结束")

mytimer = MyTimer()
mytimer.start()
mytimer.stop