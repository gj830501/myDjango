#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : indexService.py
# @Author: Eddie
# @Date  : 2017/11/17 16:18
# @Desc  : 首页业务处理类
from ailb import models
import logging
from datetime import datetime

class indexService(object):
    def __init__(self):
        pass

    #查找文章默认提取最近五条
    @classmethod
    def getEssayInfo(self,start,id):
        if id ==None :
            if start == 0:
                techEssays = models.TechEssay.objects.filter(id__lt=10  ).order_by('-id')
            else:
                end = start + 5
                techEssays = models.TechEssay.objects.filter(id__gt=self ).filter(id__lt=end).order_by('-id')
            return techEssays
        else:
            techEssay = models.TechEssay.objects.filter(id=id )
            return techEssay


    def addFavor(self,id):
        try:
            techEssay = models.TechEssay.objects.get(id=id)
            favor = techEssay.favor
            techEssay.favor=favor+1
            techEssay.save()
        except Exception as e:
            logging.error('点赞失败：',e)
            return False,e
        return True,favor

    # 更新阅读数
    def upviewNum(self,id):
        try:
            techEssay = models.TechEssay.objects.get(id=id)
            viewNum = techEssay.viewNum
            techEssay.viewNum=viewNum+1
            techEssay.save()
        except Exception as e:
            logging.error(' 更新阅计数失败:',e)
            return False

        return True

    #查询评论回复信息
    def searchReply(self,essayId):
        te = models.replyEssay.objects.filter(techEssay_id=essayId).order_by("-id")
        return  te


    #保存评论回复
    def saveReply(self,essayId,replyMes):
        te =  models.TechEssay.objects.get(id=essayId)
        rep = models.replyEssay(replyDetail=replyMes,techEssay=te)
        rep.save()
        return True



