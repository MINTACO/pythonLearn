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
# with open('./test.txt', 'r', encoding = 'UTF-8') as f:
#     # for line in f.readlines():
#     #     print(line.strip()) # 把末尾的'\n'删掉
#     print(f.readlines()[1])

# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉



# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。



# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
with open('./avatar.jpg', 'rb') as f:
    print(f.read())
