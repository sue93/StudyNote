#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-26 11:28:36
# @Author  : sue (2315172434@qq.com)
# @Link    : http://www.sevencolorhhy.com
# @Version : $Id$


# /**
#  * 装饰器函数在模块导入时，就执行。普通函数调用时就执行
#  */

def register(func):
    print('running register(%s)'%func)
    registy.append(func)
    return func

@register
def f1():
    print('running f1()')






#标准库中的装饰器
#functools.lru_cache(maxsize=128,typed=Fals) 做备忘录
#他把耗时的函数结果保存起来，避免传入相同参数，重复计算
#参数 maxsize:表示缓存多少个结果，缓存满了之后，扔掉旧的结果，最好设置成2的幂
#参数:typed 表示不同类型参数，是否分开存放
#
#








