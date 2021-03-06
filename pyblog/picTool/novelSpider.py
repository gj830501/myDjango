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
import json
import gzip


class novelSpider:
    jsList = []
    #init method
    def __init__(self,url):
        self.url = url
        self.links =[]

    #直接提取网页内容

    def catchPageContent(self):
        htmla = urllib.request.urlopen(self.url)
        htmcont = htmla.read()
        print("========================")
        print(htmcont)
        file = open('E:/page.html', 'w')
        file.write(str(htmcont))
        file.close()
        #data = json.loads(htmcont)
        #newsList = data['data']
       # for news in newsList:
        #    print(news)



    def getContent(self):
        url =self.url
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

       # req.add_header('Accept-Encoding', 'gzip')
        req.add_header("Accept-Languaget", 'zh-CN')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Cookie','UM_distinctid=15febe6e431fd-0f461420153d85-6010107f-100200-15febe6e432440; CNZZDATA1259329227=1202118421-1511490102-%7C1511490102; Hm_lvt_1538a242553b02567eac96f751f59fa8=1511491301; Hm_lpvt_1538a242553b02567eac96f751f59fa8=1511491301')
        req.add_header("User-Agent", random_header)
        req.add_header("GET", url)
        req.add_header("Host", "qxs.la")
        #req.add_header("Referer", "https://www.toutiao.com/ch/news_hot/")
        content = urllib.request.urlopen(req).read()
        #print(content)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content)
        #print(soup.prettify())
        return soup.findAll('ul',{'class':'list_content'})


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
    # http://qxs.la/dushi/
    ns = novelSpider('http://qxs.la/dushi/')
    #ns.catchPageContent()

    str = ns.getContent()[0]
    a = 1
    for l in str.select('li'):
        print(l)

        if a > 3:
            print(l.string)
        else:
            print(l.a.string)
            print(l.a.get('href'))

        a = a+1


    #tempstr = str.replace('href=\"','target=\"_self\"  href=\"http://qxs.la/dushi')
    #print(tempstr)
