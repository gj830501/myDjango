from django.contrib import admin

# Register your models here.
from .models import UserProfile,Article

#配置类  暂不起作用
class ArticleAdmin(admin.ModelAdmin):
    #控制查询列表显示列
    list_display = ('articleName', 'articleContext','add_time')
    # 控制管理界面是否可显示字段进行编辑
    fields=['articleName', 'articleContext']

admin.site.register(UserProfile,)
admin.site.register(Article,ArticleAdmin)