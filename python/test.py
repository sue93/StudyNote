#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-26 11:28:36
# @Author  : sue (2315172434@qq.com)
# @Link    : http://www.sevencolorhhy.com
# @Version : $Id$


import os
import sys
import inspect
import time
from win32com.client import DispatchEx

# ie=DispatchEx('InternetExplorer.Application')
# ie.Visible=1
# url='http://www.baidu.com'
# ie.Navigate(url)
# time.sleep(5)
# document=ie.Document
# content = document.documentElement.innerHTML

# print(content)
# ie.Quit()

import sys
s='美团'
print(sys.getsizeof(s))