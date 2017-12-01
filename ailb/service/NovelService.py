#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : NovelService.py
# @Author: Eddie
# @Date  : 2017/11/27 16:01
# @Desc  : 小说处理类
from pyblog.picTool.novelSpider import novelSpider
from ailb.viewModel.Novel import NovelModel
class NovelService:
    #暂时性爬取小说网
    preNovelUrl = 'http://qxs.la'
    novelType = None
    novelInfoList = []
    def __init__(self,novelType):
        self.novelType = novelType
        self.novelInfoList = []

    #查找小说列表-直接通过爬界面HTML内嵌到见页面
    def getNovelist(self):
        ns = novelSpider(self.preNovelUrl+'/'+self.novelType+'/')
        novelHtml = ns.getContent()
        for tags in novelHtml:
            nm = NovelModel()
            a = 1
            for l in tags.select('li'):

                if a > 3:
                    nm.lastUpdate = l.string
                elif a==1:
                    nm.novelName = l.a.string
                    nm.novelUrl = self.preNovelUrl+l.a.get('href')
                elif a==2:
                    nm.lastName = l.a.string
                    nm.lastUrl = self.preNovelUrl+l.a.get('href')
                else:
                    nm.novelAuthor = l.a.string
                    nm.novelAuthorUrl = l.a.get('href')

                a = a + 1
            self.novelInfoList.append(nm)

        return self.novelInfoList
