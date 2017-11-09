# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyblog', '0003_article_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='static/article/default.png', upload_to='article/%Y/%m', verbose_name='文章图片'),
        ),
    ]