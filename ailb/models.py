__author__ = 'Administrator'
import django.utils.timezone as timezone
from django.db import models
from datetime import datetime

#技术文章类
class TechEssay(models.Model):
    essayTitle=models.CharField(max_length=30,verbose_name=u'文章标题')
    essayContext=models.TextField(verbose_name=u'文章内容')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加日期')
    image=models.ImageField(max_length=100,upload_to=u'static/ailb/essay/%Y/%m',default=u'static/ailb/essay/default.png' ,
                             verbose_name=u'文章图片')
    favor=models.IntegerField(verbose_name=u'点赞数')
    viewNum=models.IntegerField(verbose_name=u'被查看数')
    is_recommend=models.BooleanField(default=False,verbose_name=u'是否推荐')

    class Meta:
        verbose_name=u'技术文章表'
        verbose_name_plural=verbose_name
        db_table='tb_techessay'

    def __str__(self):
        return self.essayTitle

#文章回复信息
class replyEssay(models.Model):
    #文章外键
    techEssay = models.ForeignKey(TechEssay)
    replyDetail = models.CharField(max_length=1000,verbose_name=u'回复内容')
    replyDate = models.DateTimeField(default=datetime.now(),verbose_name=u'回复日期')
    class Meta:
        verbose_name=u'文章回复信息表'
        verbose_name_plural=verbose_name
        db_table='tb_replyessay'

    def __str__(self):
        return self.replyDetail



#歌曲目录
class favorMusic(models.Model):
    musicName = models.CharField(max_length=30,verbose_name=u'歌曲名')
    covers = models.ImageField(max_length=100,upload_to=u'static/ailb/favormusic/%Y/%m',default=u'static/ailb/essay/default.png' ,
                             verbose_name=u'唱片封面')
    singer = models.CharField(max_length=30,verbose_name=u'歌手名')
    album = models.CharField(max_length=30,verbose_name=u'专集名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加日期')
    class Meta:
        verbose_name = u'收藏歌曲表'
        verbose_name_plural = verbose_name
        db_table = 'tb_favormusic'

    def __str__(self):
        return self.musicName