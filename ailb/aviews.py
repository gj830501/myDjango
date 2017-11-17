from django.shortcuts import render
import logging
logging.basicConfig(level=logging.INFO)
# Create your views here.
from django.shortcuts import HttpResponse

#测试用随后删除
def test(request):
   #用HttpResponse返回字符串
    return HttpResponse('Hello ailb World!')

#首页
def index(request):

   #用HttpResponse返回字符串
    return render(request,'alib/index.html')
