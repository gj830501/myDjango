#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Novel.py
# @Author: Eddie
# @Date  : 2017/11/30 16:36
# @Desc  : 小说MODEL
from django.db import models

class NovelModel(models.Model):
    def __init__(self):
        pass
    novelName = models.CharField(max_length=50)
    novelUrl = models.CharField(max_length=20)
    lastName =  models.CharField(max_length=50)
    lastUrl = models.CharField(max_length=20)
    novelAuthor =  models.CharField(max_length=50)
    novelAuthorUrl = models.CharField(max_length=50)
    lastUpdate =  models.CharField(max_length=50)
