#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : NovelService.py
# @Author: Eddie
# @Date  : 2017/11/27 16:01
# @Desc  : 小说处理类
from pyblog.picTool.novelSpider import novelSpider
class NovelService:
    #暂时性爬取小说网
    novelUrl = 'http://qxs.la/dushi/'

    #查找小说列表-直接通过爬界面HTML内嵌到见页面
    def getNovelist(self):
        ns = novelSpider(self.novelUrl)
        novelHtml = ns.getContent()
        return novelHtml
