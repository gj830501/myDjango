"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pyblog import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from ailb import aviews

#web后台用户名密码：gujun/gujunfox
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #自己的路由
    url(r'^index/', views.index),
    url(r'^add/$', views.add),
    url(r'^add/(\d+)/(\d+)/$', views.add2),
    url(r'^list/', views.list),
    url(r'^demo/', views.demo),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'),name='login'),
    url(r'^signup/$', TemplateView.as_view(template_name='signup.html'), name='signup'),
    url(r'^loginin/', views.login),
    url(r'^regist/', views.regist),
    url(r'^logout/', views.logout),
    url(r'^userArticleContent/', views.userArticleContent),
    url(r'^updateArticel/', views.updateArticel),
    ####   以下是AILB 项目URL配置信息  ###
    url(r'^test/', aviews.test),
    url(r'^ailb/index', aviews.index),
    url(r'^ailb/essayFavor/', aviews.essayFavor),
    url(r'^ailb/detail/id(\d+)/$', aviews.detail),
    url(r'^ailb/replySubmit/', aviews.replySubmit),
    url(r'^ailb/novel/', aviews.novel),


]
handler404 = TemplateView.as_view(template_name='error.html')