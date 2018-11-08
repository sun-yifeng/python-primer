# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/8 2:01 AM
# @Author: sunyf
# @File  : FuntionDemo.py

""" 形参和实参  """
print("----形参和实参----")
#定义的变量（形参）
def myFirstFuntion(name):
    """
    我是说明文档1->
    我是说明文档2->
    """
    print("hello " + name + "!")
    return

#实际的参数（实参）
for i in range(5):
    myFirstFuntion("sunyf");

"""  函数文档  """
print("-----函数文档-----")
help(myFirstFuntion)
#myFirstFuntion.__doc__

"""  关键字参数  """
print("-----关键字参数-----")
def saySomething(name, words):
    print(name + ", " + words)
saySomething(name="sun", words="yf")


"""  默认参数  """
print("-----默认参数（位置参数）-----")
def sayAnything(name="sun", words="yifeng"):
    print(name + ", " + words)
sayAnything(name="fan", words="bingbing")
sayAnything()

""" 收集参数 """
print("-----收集参数-----")
def testParam1(*args):
    print("有 %d 个 参数" % len(args))
    print("第 2 个参数是:", args[1])
testParam1("sun", "yi", "feng")

print("-----默认参数（位置参数）-----")
def testParam2(*args, pos):
    print("收集参数是:", args)
    print("位置参数是:", pos)
testParam2("sun", "yi", "feng", pos="fan")

"""  打包解包  """
print("-----打包解包-----")
a = [1, 2, 3, 4, 5, 6]
#testParam1(a)
testParam1(*a)

""""   全局变量在函数内部不能修改  """
print("-----全局变量在函数内部不能修改-----")
global_var = 100
def discount(price, rate):
    total_price = price * rate
    global_var = 10
    print("全局变量修改之后的值1:", global_var)
    return total_price
total_price1 = discount(100, 0.5)
print(total_price1)
print("全局变量修改之后的值2:", global_var)

""" global修改全局函数 """
print("------global修改全局函数-----")
global_var1 = 9
def myFuntion():
    #print("修改之前的值：", global_var1)
    global global_var1
    global_var1 = 3
    print("函数内部的值：", global_var1)
myFuntion()
print("全局变量的值：", global_var1)