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
from collections.abc import Iterable
from collections.abc import Iterator
import functools
import time

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def trim(s):
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s

#myDict = {'name':'lushuo','age':23,'job':'coder'}
# for key,value in myDict.items():
#     print(key,value)
#print(isinstance([1,2,3],Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对
#for i,value in enumerate(['A','B','C']):
    #print(i,value)

#斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

#杨辉三角
# 1
# 11
# 121
# 1331
# 14641
# def triangle(max):
#     yield([1])
#     L = [1,1]
#     yield(L)
#     n = 0
#     while n < max - 2:
#         L1 = [1]
#         for i in range(1,len(L)):
#             L1.append(L[i-1]+L[i])
#         L1.append(1)
#         L = L1
#         yield(L1)
#         n = n + 1
#     return 'done'

# g = triangle(10)

# while True:
#     try:
#         x = next(g)
#         print(x)
#     except StopIteration as e:
#         print(e.value)
#         break

# def log(text=''):
#     def decorator(func):
#         print(1)
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('begin call',text)
#             func(*args,**kw)
#             print('end call',text)
#         return wrapper
#     return decorator

# @log('hello')
# def normalize(name):
#     print(name.capitalize())

# normalize('darren')

# A = None
# print(A)
# def test():
#     global A
#     A = 100
# test()
# print(A)


# while True:
#     b = input('type something:')
#     if b == '1':
#         continue
#     else:
#         pass
#     print('still in while')

# print('finish while')

# a = [1,2,3]
# b = [4,5,6]
# print(list(zip(a,b)))
# for i, j in zip(a, b):
#     print(i/2, j*2)

# def fun1(x, y):
#     return x+y
# fun2 = lambda x,y: x*y
# result = list(map(fun1, [1,2,3], [2,2,3]))
# print(result)

from copy import *
a = [1,2,3,[5,6]]
b = copy(a) 
c = deepcopy(a)
# id()查看硬盘中的索引
print(id(a[3]))
print(id(b[3]))
print(id(c[3]))