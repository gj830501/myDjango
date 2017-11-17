# -*- coding: utf-8 -*-
# 一个简单的re实例，匹配字符串中的hello字符串

# 导入re模块
import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'\s*[\w|\n]*location.\w+="/([\w|/|.]*)"?')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
str='main.js?v=1510123324000'
pattern = re.compile(r'\w+.js?')
match3 = re.search(pattern,str)
print(match3.group(0))


contactInfo = 'Doe, John: 555-1212'
match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
print('======================')
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.group(3))

content="""

/**
 * Created by flyjennyetn on 2016/2/1.
 */
requirejs.config({
    waitSeconds: 0,
    map:{
        '*':{
            'style':'js/require/css'
        }
    },
    baseUrl: "./",
    paths: {
        'requireLib':'js/require/require',
        "text": 'js/require/text',
        "jquery": "js/jquery/jquery",
        "jquery_form":'js/jquery/jquery.form',
        "md5": "js/jquery/jquery.md5",
        "cookie": "js/jquery/jquery.cookie",
        "layer_": "js/layer/layer",
        "laydate": "js/laydate/laydate",
        "laypage": "js/laypage/laypage",
        "slide": "js/jquery/jquery.SuperSlide.2.1.1",
        "avalon": "js/avalon/avalon.shim",
        "avalonGetModel": "js/avalon/avalon.getModel",
        "mmRequest": "js/avalon/mmRequest",
        "mmPromise": "js/avalon/mmPromise",
        "mmHistory": "js/avalon/mmHistory",
        "mmRouter": "js/avalon/mmRouter",
        "mmState": "js/avalon/mmState",
        "myfilter":"js/filter/myfilter"
    },
    shim: {
        avalon: {
            exports: "avalon"
        },
        md5:{
            deps: ['jquery'],
            exports: 'md5'
        },
        cookie:{
            deps: ['jquery'],
            exports: 'cookie'
        },
        laydate:{
            deps: ['jquery','style!js/
            resolve(avalon.templateCache[url] = tpl)
        })
    }
    requirejs(["js/router.js?v="+vTime])
        "layer_": "js/layer/layer",
"""
#"[:|\s]+"(\w+\S+\w+\S*")
pattern4 = re.compile(r'[\s|\n|"]*[\w|\(|\[|_]+')
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
m = re.search(pattern4,content)
print("此文本内容中包括JS如下：", m)
print(m.group(0))