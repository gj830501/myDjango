__author__ = 'Administrator'
import urllib.request
from gzip import GzipFile
import string, os, sys
from io import StringIO
import zlib

def loadData(url):
    request = urllib.request.Request(url)
    request.add_header('Accept-encoding', 'gzip,deflate')
    response = urllib.request.urlopen(request)
    content = response.read()
    encoding = response.info().get('Content-Encoding')
    if encoding == 'gzip':
        content = gzip(content.decode('iso-8859-1'))
    elif encoding == 'deflate':
        content = deflate(content)
    return content

def gzip(data):
    buf = StringIO(data)
    f = gzip.GzipFile(fileobj=buf)
    return f.read()

def deflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)

def main():
    url = "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1B5AAA1B136D93&cp=5A11960DC9C3BE1"
    content = loadData(url)
    print (content)

if __name__ == '__main__':
    main()
