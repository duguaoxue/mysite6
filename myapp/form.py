__author__ = 'w'
# coding=utf-8
from django import forms
class UserloginForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput)
class UserregistForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput)
#class IndexForm(forms.Form):

