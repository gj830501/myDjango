from django.shortcuts import render
import logging
logging.basicConfig(level=logging.INFO)
# Create your views here.
from django.shortcuts import HttpResponse
from pyblog import models
from django.template import RequestContext
from django.contrib import auth
from  pyblog.form.loginForm import LoginForm
from pyblog.form.userRegistForm import userRegistForm
from django.contrib.auth.hashers import make_password, check_password
from django.db.models.functions import Substr
import json
from django.core import serializers

def index(request):
   #用HttpResponse返回字符串
    #return HttpResponse('Hello World!')
    #用DJANGO render 返回页面
    logging.info('user login index')
    #TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    #info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    #return render(request,'index.html', {'TutorialList': TutorialList})
    #persons=models.Person.objects.all()
    #return render(request, 'index.html', {'TutorialList': persons})
    articles = models.Article.objects.all().order_by('add_time' )

    for articel in articles:
        print(Substr(articel.articleContext, 1, 10))

    return render(request,'index.html', {'articles':articles})

def add(request):
    logging.info('user get')
    a=request.GET['a']
    b=request.GET['b']
    return HttpResponse(a+b)

def add2(request,a,b):
    logging.info('user add2-a-b:'+a+' '+b)
    return HttpResponse(a+b)

def list(request):
    logging.info('user login list')
    List = map(str, range(100))  # 一个长度为100的 List
    pserson=models.Person(name='gujunfox', age=34)
    logging.info(u'创建一个新用户')
    pserson.save()
    return render(request, 'example/list.html', {'List': List})

def demo(request):
    logging.info('user demo ')
    return render(request, 'dream-web-template/index.html')

#user login sys
def login(request):
    name=request.POST['username']
    password=request.POST['password']
    form = LoginForm(request.POST)
    #pp =make_password("123456", None, 'pbkdf2_sha256')
    #print('密码明文加密：',pp )
    #print('密码明文解密：', check_password('123456', pp))
    if form.is_valid():
        print(form.cleaned_data['username'])
        user = auth.authenticate(username=name, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            #登录成功跳转用户文章列表

            userArticles = models.Article.objects.all().filter(user_id=user.id)

            return render(request,'userArticelist.html',{'userArticles':userArticles})

    #user=models.UserProfile.objects.get(username=name)
    logging.info("user to login"+request.method)
    return render(request,'login.html',{'msg':u'用户名密码错误，请检查！'})

#user regist
def regist(request):
    userInfoForm = userRegistForm(request.POST)
    if userInfoForm.is_valid():
        print('check pass')
        user = models.UserProfile(username=userInfoForm.cleaned_data['username'],nick_name=userInfoForm.cleaned_data['nick_name'],
        birth=userInfoForm.cleaned_data['birth'],email=userInfoForm.cleaned_data['email'],
        password=make_password(userInfoForm.cleaned_data['password'], None, 'pbkdf2_sha256'))
        user.save()
        return render(request, 'login.html', {'msg': u'用户注册成功，请重登录！'})

    errorInfo = userInfoForm.errors
    print(u'注册信息有误，请检查！')
    return render(request,'signup.html',{'errorInfo':errorInfo})

#用户注销
def logout(request):
    auth.logout(request)
    return render(request,'login.html')

def userArticleContent(request):
    logging.info('userArticleContent')
    articleId = request.POST['id']
    userArticle = models.Article.objects.all().filter(id=articleId)
    result = serializers.serialize("json", userArticle)
    return HttpResponse(result, content_type='application/javascript')


def updateArticel(request):
    articleId = request.POST['articleId']
    articleName = request.POST['articleName']
    articleContent =  request.POST['articleContext']
    models.Article.objects.filter(id=articleId).update(articleContext=articleContent)
   # userArticle.articleName=articleName
   # userArticle.articleContent = articleContent
   # userArticle.save()
    userArticles= models.Article.objects.all()
    return render(request, 'userArticelist.html', {'userArticles': userArticles})