# -*- coding: utf-8 -*-

"""
==================================================
   File Name：     base_test.py
   email:         songdongdong@weidian.com
   Author :       songdongdong
   date：          2020/7/24 18:11
   Description :  
==================================================
"""

import struct

a = 12
# 将a变为二进制

bytes = struct.pack('i', a)
# 此时bytes就是一个string字符串，字符串按字节同a的二进制存储内容相同。
print(bytes)

# 再进行反操作 ，现有二进制数据bytes，（其实就是字符串），将它反过来转换成python的数据类型：

a, = struct.unpack('i', bytes)
print(a)
# 注意，unpack返回的是tuple，所以如果只有一个变量的话：

bytes = struct.pack('i', a)

# 那么，解码的时候需要这样

a, = struct.unpack('i', bytes)
(a,) = struct.unpack('i', bytes)

# 如果直接用a=struct.unpack('i',bytes)，那么 a=(12.34,) ，是一个tuple而不是原来的浮点数了。
