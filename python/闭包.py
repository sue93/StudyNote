#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-29 14:21:42
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

# /**
#  * 代码会报错。原因是,python编译函数的定义体时，他判断b是局部变量。但是在print(b)前又没有定义
#  */

b=5
def test(a):
    global b          #要加上这句，才对
    print(a)
    print(b)
    b=10

p=test(3)


l=[1,2,3]

#闭包，是指延伸了作用域的函数
#
#
#有一个，场景，如果我们要计算股票的平均值。股票每天都会变动


def fj_avg():
    series=[]
    def avg(price):
        series.append(price)
        total=sum(series)
        num=len(series)
        return total/num
    return avg


f=fj_avg()
print(f(10))

print(f(100))





#上面的方法会记录所有的历史变量，太浪费内存
def fj_avg_new():
    total=0
    num=0
    def avg(price):
        nonlocal total,num               #要声明为自由变量，否则报错。我们在avg函数为total或num赋值，会把他们变成局部变量，这样就不会保存在闭包里了
        total+=price
        num+=1
        return total/num
    return avg


p=fj_avg_new()
print(p(10))
print(p(20))








