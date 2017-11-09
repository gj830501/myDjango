import django.utils.timezone as timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
#person用户类
@python_2_unicode_compatible
class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.CharField(max_length=50,default='aa')
    #birthday=models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.name


class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=40,default=u'',verbose_name=u'昵称')
    birth = models.DateTimeField(verbose_name=u'生日',null=True,blank=True)
    gender=models.CharField(max_length=5,choices=(('male',u'男'),('female',u'女')),default='male'
                            ,verbose_name=u'性别')
    address=models.CharField(max_length=100,verbose_name=u'地址',default=u'')
    mobile = models.CharField(max_length=100,null=True,blank=True,verbose_name=u'手机号')

    class Meta:
        verbose_name=u'用户信息表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username

class Article(models.Model):
    user = models.ForeignKey(UserProfile)
    articleName=models.CharField(max_length=30,verbose_name=u'文章标题')
    articleContext=models.TextField(verbose_name=u'文章内容')
    add_time=models.DateTimeField(default=datetime.now)
    image=models.ImageField(max_length=100,upload_to=u'article/%Y/%m',default=u'static/article/default.png' ,
                            verbose_name=u'文章图片')

    class Meta:
        verbose_name=u'文章信息表'
        verbose_name_plural=verbose_name
        db_table='t_article'

    def __str__(self):
        return self.articleName
