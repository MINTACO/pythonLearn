#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo.py
@Time    :   2019/12/18 17:08:48
@Author  :   Darren 
@Version :   1.0
@Contact :   734876157@qq.com
@License :   (C)Copyright 2019-2020, Darren
@Desc    :   None
'''

# here put the import lib
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

_param = (1,2,3,4)
print(calc(_param))


