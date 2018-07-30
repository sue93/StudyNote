#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-26 11:53:34
# @Author  : sue (2315172434@qq.com)
# @Link    : http://www.sevencolorhhy.com
# @Version : $Id$
#/* 静态方法和类方法区别*/
import os

class Foo(object):
	def instance_method(self):
		print("实例方法,只能别对象实例调用")

	@staticmethod                           #继承不被重写
	def static_method():
		print("静态方法")

	@classmethod
	def class_method(cls):					
		print("类方法")

