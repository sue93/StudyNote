#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-26 11:28:36
# @Author  : sue (2315172434@qq.com)
# @Link    : http://www.sevencolorhhy.com
# @Version : $Id$

import re    #主要用于字符串匹配
msg="xing dao shui qiong chu zuokanyunqishi"
rst = re.search(r'[1‐9]\d{5}', 'BIT 1000814')

print(rst.group(0))
print(rst.string)