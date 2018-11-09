# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 11:09 PM
# @Author: sunyf
# @File  : BeautSoup.py

import urllib.request
import re
from bs4 import BeautifulSoup

"""  

一个灵活又方便的网页解析库，处理高效，支持多种解析器。
利用它就不用编写正则表达式也能方便的实现网页信息的抓取

"""
def main():
    url = "http://baike.baidu.com/view/284853.htm"
    res = urllib.request.urlopen(url)
    html = res.read()
    soup = BeautifulSoup(html, "html.parser")

    for each in soup.find_all(href=re.compile("view")):
      print(each.text, "->", ''.join(["http://baike.baidu.com", each["href"]]))

if __name__ == '__main__':
    main()
