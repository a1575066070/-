# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:24:44 2020

@author: tute
"""

try:
    x = input('被除数：')
    y = input('除数：')
    z = int(x) / int(y)
except ValueError:
    print('请输入数字!')
except ZeroDivisionError:
    print('除数不能为0!')
else:
    print(x, "/", y, "=", z)