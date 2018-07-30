#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-26 11:28:36
# @Author  : sue (2315172434@qq.com)
# @Link    : http://www.sevencolorhhy.com
# @Version : $Id$

import os
def add_number(func):
	def adder(arg):
		return func(arg)+100
	return adder
@add_number
def pingfang(x):
	return x*x


print(pingfang(20))