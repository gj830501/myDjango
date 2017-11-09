#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : userRegistForm.py
# @Author: Eddie
# @Date  : 2017/11/6 10:37
# @Desc  : user's info

from django import forms

class userRegistForm(forms.Form):
    username = forms.CharField(required=True,min_length=4)
    nick_name = forms.CharField(required=False)
    birth = forms.DateTimeField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=6)
    confirm_password = forms.CharField(required=True, min_length=6)
    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise forms.ValueError(u'两次密码不一致')
        cleanded_data = super(userRegistForm,self).clean()
        return cleanded_data
