#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Eddie
# @Date  : 2017/11/9 8:58
# @Desc  :
import os
#判断文件类型目前是图片
def strpbrk(fileName):
    for c in ['.jpg','.JPG','.png','.bmp','.BMP']:
        _index = fileName.find(c)
        if _index > -1:
            return True
    return False

str = 'C:\\Users\Public\\Pictures\\Sample Pictures'

filelist = os.listdir(str)
print(filelist)
for x in filelist:
    print(strpbrk(x))
