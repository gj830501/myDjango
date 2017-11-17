from django.contrib import admin

# Register your models here.
from .models import TechEssay
#注册到DJANGO 管理模块中，前期方便添加文章
class TechEssayAdmin(admin.ModelAdmin):
    #控制查询列表显示列
    list_display = ('essayTitle', 'essayContext', 'add_time')
    # 控制管理界面是否可显示字段进行编辑
    #fields=['articleName', 'articleContext']

admin.site.register(TechEssay,TechEssayAdmin)
