
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : piClassify.py
# @Author: Eddie
# @Date  : 2017/11/8 14:01
# @Desc  : 自动扫描目录下所有照片，进行分类存储
from PIL import Image
import os
from PIL.ExifTags import TAGS
import shutil
import random

class imageClassify(object):
    #初始化信息
    def __init__(self, picPath,bakPath):
        self.picPath = picPath
        self.bakPath = bakPath
        self.picLists = []
        self.folders = []
    #扫描路径区分照片及文件夹
    def scanDir_pic(self):

        os.chdir(self.picPath)
        print('更换路径后目录:', os.path.abspath('.'))
        curPath = os.path.abspath('.')
        print('输入路径下文件名：',os.listdir('.'))
        listdirs = os.listdir('.')
        for tempName in listdirs:
            tempCurPath = os.path.join(curPath,tempName)
            if os.path.isfile(tempCurPath):
                #暂时过滤掉除不是照片的文件
                if self.strpbrk(tempCurPath):
                    self.picLists.append(tempCurPath)
            elif os.path.exists(tempCurPath):
                self.folders.append(tempCurPath)
        self.getPicInfo()
        #清空当前文件LIST再循环文件夹
        self.picLists=[]
        try:
            if len(self.folders)==0:
                return
            for index in range(len(self.folders)):
                print('index='+str(index),self.folders[index])
                nextHandleFold= self.folders[index]
                #文件夹列表清除要处理的nextHandleFold
                self.folders.pop(index)

                #更新当前目录
                self.picPath=nextHandleFold
                self.scanDir_pic()
        except Exception as e:
            print('文件夹列表循环异常:',e)

        #print(len(self.folders))

    #取照片信息
    def getPicInfo(self):
        print("照片归类处理方法")
        for pic in self.picLists:
            im = Image.open(pic)
            info = im._getexif()
            #无法获取信息的给出默认文件夹(大点的日期)
            if info is None:
                date = '2020-01-01'
                im.close()
                self.classify(pic, date)
                return
            try:
                for tag, value in info.items():
                    #退过信息标签为DATETIME取出照片日期
                    decoded = TAGS.get(tag, tag)
                    if decoded == 'DateTime':
                        date = value
                        print('picName:',pic,'  picDate:',date)
                        im.close()
                        self.classify(pic , date)
                        break
            except Exception as e:
                print('获取信息出现异常')
                print(e)
        return




    #照片分类处理方法按年-月存储
    def classify(self,picAbsPath,date):
        print('照片分类处理方法开始')
        #创建一个归档照片的根目录不作过多判断
        if os.path.exists(self.bakPath):
            print('根目录 已存在')
        else :
            os.mkdir(self.bakPath)
        #创建一个归档照片的根目录不作过多判断
        if os.path.exists(self.bakPath+'/dupli'):
            print('根目录 已存在')
        else:
            os.mkdir(self.bakPath+'/dupli')
        #切换到备份要目目录
        os.chdir(self.bakPath)
        datestrList =[]
        if date.index(':'):
            datestrList = date.split(':')
        elif date.index("-"):
            datestrList = date.split('-')
        elif date.index('/'):
            datestrList = date.split('/')
        #年目录名
        firfoldName = datestrList[0]
        #月目录名
        secfoldName = datestrList[1]
        if os.path.exists(firfoldName):
            pass
        else:
            os.mkdir(firfoldName)
        os.chdir(firfoldName)
        if os.path.exists(secfoldName):
            pass
        else:
            os.mkdir(secfoldName)
        os.chdir(secfoldName)

        print(os.path.abspath('.'),'==',picAbsPath)
        #shutil.move(picAbsPath, random.randint(1,9999999999))
        #判断文件名是否重复
        try:
            shutil.move(picAbsPath, '.')
        except Exception:
             baseName = os.path.basename(picAbsPath)
             newName = str(random.randint(1,100))+baseName
             newAbsPath = picAbsPath.replace(baseName, newName)
             #os.rename(picAbsPath, newAbsPath)
             shutil.copyfile(picAbsPath,self.bakPath+'/'+newName)
             print('copyfile:',picAbsPath,newName)
        return


    #判断文件类型目前是图片
    @staticmethod
    def strpbrk(fileName):
        for c in ['.jpg','.JPG','.png','.bmp','.BMP']:
            _index = fileName.find(c)
            if _index > -1:
                return True
        return False


if __name__=='__main__':
    #pycharm不支持
    #path = raw_input('enter the path of you scan:')
    path = input('输入需要整理照片根目录：')
    bakPath =  input('输入照片整理到目录：')
    img = imageClassify(path,bakPath)
    img.scanDir_pic()

