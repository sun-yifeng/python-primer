# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/10 12:09 AM
# @Author: sunyf
# @File  : TkinterDemo.py

import tkinter as tk

""" GUI 的最终选择 Tkinter """

class App:

    def __init__self(self, root):
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame, text = "打招呼", fg = self.say_hi)
        self.hi_there.pack(side = tk.LEFT)

    def say_hi(self):
        print("大家好！")

root = tk.Tk()
app = App(root)

root.mainloop()
