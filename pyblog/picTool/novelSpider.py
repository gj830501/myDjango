#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : novelSpider.py
# @Author: Eddie
# @Date  : 2017/11/9 13:47
# @Desc  : 网上小说爬取

from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import os
import re
import random
import chardet
import zlib
import json

class novelSpider:
    jsList = []
    #init method
    def __init__(self,url):
        self.url = url
        self.links =[]

    #直接提取网页内容

    def catchPageContent(self):
        htmla = urllib.request.urlopen(self.url)
        htmcont = htmla.read().decode('utf-8')
        print("========================")
        print(htmcont)
        data = json.loads(htmcont)
        newsList = data['data']
        for news in newsList:
            print(news)




    @staticmethod
    def getContent(url):
        """
        此函数用于模拟浏览器访问的网页
        """
        headers = [
            'MMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400']
        random_header = random.choice(headers)

        """ 
        对于Request中的第二个参数headers，它是字典型参数，所以在传入时 
        也可以直接将个字典传入，字典中就是下面元组的键值对应 
        """
        req = urllib.request.Request(url)
        req.add_header('Accept', 'text/javascript, text/html, application/xml, text/xml, */*')

        req.add_header('Accept-Encoding', 'gzip')
        req.add_header("Accept-Languaget", 'zh-CN')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Cookie','tt_webid=6490058021534975501; uuid="w:2ab0c434e740430cb730692b57cf4c6b"; UM_distinctid=15fd3a7972337c-0a41b4de85bfc8-1c1f7d54-100200-15fd3a79724337; __tasessionId=r6d8e2t9k1511091592686; CNZZDATA1259612802=2107586991-1511081791-%7C1511087191')
        req.add_header("User-Agent", random_header)
        req.add_header("GET", url)
        req.add_header("Host", "www.toutiao.com")
        req.add_header("Referer", "https://www.toutiao.com/ch/news_hot/")
        print('====', req.headers)

        content = urlopen(req).read()
        print(content)

    #查找JS源文件内容
    def downJs(self,jsUrl):
        jsSource = urllib.request.urlopen(self.url+jsUrl)
        jsContent = jsSource.read().decode('utf-8')
        #print(jsContent)

        if self.saveFileContent(jsUrl,jsContent):
            print('文件保存成功：',jsUrl)
            #解析文本内容中是否有JS
            self.compiJsbyRe(jsContent)
            return True
        else:
            print('文件保存失败')
            return False

        # 按正则表达式解析出js文件
    def compiJsbyRe(self, content):
        # 'requireLib':'js/require/require',
        # "text": 'js/require/text',
        pattern = re.compile(r'\s+\wjs/\w*')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        m = pattern.search(pattern,content)
        print("此文本内容中包括JS如下：",m)

    #根据源文件路径再保存到相应该文件夹下
    def saveFileContent(self,url,htmlstr):
        rootPath='E:\eddie\Python\jklife'
        os.chdir(rootPath)
        #解释传入路径  如：js/require/require.js
        filePath = url.split('/')
        for x in filePath:
            #如果找到.js结尾说明那是文件名
            if x.find('.js')>0:
                fineName = x
                pattern = re.compile(r'\w+.js?')
                match = re.search(pattern, x)
                file = open(match.group(0),'w')
                file.write(htmlstr)
                file.close()
                return True
            #创建文件夹
            if os.path.exists(x):
                os.chdir(x)
            else:
                os.mkdir(x)
                os.chdir(x)
        return False








if __name__=='__main__':
    ns = novelSpider('https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source='
                     'toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1B5AAA1B136D93&cp=5A11960DC9C3BE1')
    ns.catchPageContent()
    #novelSpider.getContent('https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1B5AAA1B136D93&cp=5A11960DC9C3BE1')


