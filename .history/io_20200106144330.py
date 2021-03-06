#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'IO'

__author__ = 'Darren Lu'

# 功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。


# 读文件
# try:
#     f = open('./test.txt','r')
#     s = f.read()
# # 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
# finally:
#     if f:
#         f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('./test.txt', 'r') as f:
    print(f.read())

# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。