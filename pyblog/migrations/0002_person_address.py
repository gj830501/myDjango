# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default='aa', max_length=50),
        ),
    ]