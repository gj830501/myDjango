from django.shortcuts import render
import logging
logging.basicConfig(level=logging.INFO)
# Create your views here.
from django.shortcuts import HttpResponse
from ailb.service.indexService import indexService
import logging
import simplejson
from django.core import serializers
from  ailb.service.NovelService import NovelService

#测试用随后删除
def test(request):
   #用HttpResponse返回字符串
    return HttpResponse('Hello ailb World!')

#首页
def index(request):
    indexServiceIns = indexService()
    techEssays = indexServiceIns.getEssayInfo(0,None)
    toutiaoNewsList = indexServiceIns.getNewsInfo()
    replyList = indexServiceIns.searchReply(-1)

    #用HttpResponse返回字符串
    return render(request,'alib/index.html',{'techEssays':techEssays,'toutiaoNewsList':toutiaoNewsList,'replyList':replyList})


#点赞
def essayFavor(request):
    id=request.POST['id']
    logging.info('点赞ID：'+id)
    iservice = indexService()
    result ={}
    flag,info =iservice.addFavor(id)
    if flag:
        #简单返回用simplejson，如果返回对像需序列化用serializers
        result = simplejson.dumps( info)
    else:
        result  = simplejson.dumps( 'error',info)
    return HttpResponse(result, content_type='application/javascript')

#查看详细内容
def detail(request,id):
    indexServiceIns = indexService()
    techEssay = indexServiceIns.getEssayInfo(0,id)
    if indexServiceIns.upviewNum(id):
        te = indexServiceIns.searchReply(id)
        return render(request,'alib/view.html',{'techEssay':techEssay,'te':te})
    else:
        return  HttpResponse('查看详细内容后台更新出错啦!')

#评论回复提交
def replySubmit(request):
    id = request.GET['id']
    mes = request.GET['replyMes']
    indexServiceIn = indexService()
    if indexServiceIn.saveReply(id,mes):
         tps = indexServiceIn.searchReply(id)
         tp=[]
         tp.append(tps[0])
         logging.info('============', serializers.serialize("json", tp))
         result = serializers.serialize("json", tp)
         return HttpResponse(result, content_type='application/json')
    else:
        return  HttpResponse('评论回复后台更新出错啦!')


#查看小说列表
def novel(request,novelType):
    logging.info('查看小说列表'+novelType)
    ns = NovelService(novelType)
    novelInfoList = ns.getNovelist()

    return render(request,'alib/novel.html',{'nslist':novelInfoList})