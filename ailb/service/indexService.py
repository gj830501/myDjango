#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : indexService.py
# @Author: Eddie
# @Date  : 2017/11/17 16:18
# @Desc  : 首页业务处理类
from ailb import models
class indexService(object):

    def getEssayInfo(self,start,end):
        if start == 0 and end == 0:
            techEssay = models.TechEssay.objects.all().filter(id > 6 )
