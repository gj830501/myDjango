#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : loginForm.py
# @Author: Eddie
# @Date  : 2017/11/5 20:00
# @Desc  : cheack the info of user login
from django import forms
"""
    the method is vaild the login user's info 
    extends the Django Forms
"""
class LoginForm(forms.Form):
        username =  forms.CharField(required=True,min_length=4)
        password = forms.CharField(required=True,min_length=6)



