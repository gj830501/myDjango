__author__ = 'Administrator'
import urllib.request
import json
import random
import string
#直接提取网页内容

def catchPageContent(url):
        htmla = urllib.request.urlopen(url)
        htmcont = htmla.read().decode('utf-8')
        print("==url==",url)
        data = ""
        data = json.loads(htmcont)
        newsList = data['data']
        return newsList


def getContent(url):
    """
    此函数用于模拟浏览器访问的网页
    """
    headers = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ',
        'MMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400',
               'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
               'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16']
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
    #req.add_header('Cookie',
     #              'tt_webid=6490058021534975501; uuid="w:2ab0c434e740430cb730692b57cf4c6b"; UM_distinctid=15fd3a7972337c-0a41b4de85bfc8-1c1f7d54-100200-15fd3a79724337; __tasessionId=r6d8e2t9k1511091592686; CNZZDATA1259612802=2107586991-1511081791-%7C1511087191')
    req.add_header("User-Agent", random_header)
    req.add_header("GET", url)
    req.add_header("Host", "www.toutiao.com")
    req.add_header("Referer", "https://www.toutiao.com/ch/news_hot/")
    htmcont =urllib.request.urlopen(req).read()
    print(htmcont.decode())
    data = json.loads(htmcont)
    newsList = data['data']
    return newsList



def getToutiaoNews():
    url = "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=%s&cp=%s"
    #作为参数，实现刷新新闻内容
    param1='A1052AE1737D5E5'
    param2='5A132DD5BE555E1'
    param1 = (','.join(random.sample(['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I',
                                       'i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R',
                                       'r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','0','1',
                                       '2','3','4','5','6','7','8','9'], 15))).replace(',','')
    param2 = (
    ','.join(random.sample(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I',
                            'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R',
                            'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '0',
                            '1',
                            '2', '3', '4', '5', '6', '7', '8', '9'], 15))).replace(',', '')


    contents = getContent(url%(param1,param2))
    for news in contents:
        print(news)




if __name__=='__main__':
    getToutiaoNews()