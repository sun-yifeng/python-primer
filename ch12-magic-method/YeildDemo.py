# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/9 1:51 PM
# @Author: sunyf
# @File  : YeildDemo.py

""" 此栗子验收yeild 和 for循环的组合使用方法 """

"""
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，
但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 
的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 
yield 返回当前的迭代值。

yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算
下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰

在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接
抛出 StopIteration 终止迭代。
"""

"""
斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意数都可由前两个数相加得到，比如：
1 1 2 3 5
"""

""" 定义fibonacci函数 """
def fab(max):
    #注意此种赋值方法
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        #print(b)
        # 注意此种赋值方法
        a, b = b, a + b
        n = n + 1

""" 打印fibonacci数列 """
for i in fab(10):
    print(i)


