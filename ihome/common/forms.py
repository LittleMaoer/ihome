import re
from django import forms
from django.shortcuts import render

from common.models import User


class UserForm(forms.Form):
    # 定义表单，验证数据
    mobile = forms.CharField(required=True,
                            error_messages={'required': '请填写电话号',
                            })
    password = forms.CharField(required=True, max_length=12, min_length=1,
                               error_messages={
                                   'required': '请输入密码',
                                   'max_length': '密码不能超过12位',
                                   'min_length': '密码不能低于8位',
                               })
    password2 = forms.CharField(required=True, max_length=12, min_length=1,
                               error_messages={
                                   'required': '请输入密码',
                                   'max_length': '密码不能超过12位',
                                   'min_length': '密码不能低于8位',
                               })

    def clean(self):
        # 校验form表单的数据
        phone = User.objects.filter(phone=self.cleaned_data.get('mobile')).first()
        if phone:
            raise forms.ValidationError({'mobile': '该账号已注册，请更换账号'})
        pwd1 = self.cleaned_data.get('password')
        pwd2 = self.cleaned_data.get('password2')
        if pwd1 and pwd2:
            if pwd1 != pwd2:
                raise forms.ValidationError({'password2': '两次输入密码不一致'})
        return self.cleaned_data


class LoginForm(forms.Form):
    mobile = forms.CharField(required=True, error_messages={'required': '请输入电话号'})
    password = forms.CharField(required=True, error_messages={'required': '请输入密码'})

    def clean(self,):
        phone = User.objects.filter(phone=self.cleaned_data.get('mobile')).first()
        if not phone:
            error = '账号不存在,请重新输入或注册'
            raise forms.ValidationError({'mobile': error})
        if self.cleaned_data.get('password') != phone.pwd_hash:
            error = '密码不正确'
            raise forms.ValidationError({'password': error})
        return self.cleaned_data


class HouseForm(forms.Form):
    title = forms.CharField(required=True, max_length=64)
    price = forms.IntegerField(required=True)
    area_id = forms.IntegerField(required=True)
    address = forms.CharField(required=True, max_length=512)
    room_count = forms.IntegerField(required=True)
    acreage = forms.CharField(required=True, max_length=64)
    unit = forms.IntegerField(required=True)
    capacity = forms.IntegerField(required=True)
    beds = forms.CharField(required=True, max_length=64)
    deposit = forms.IntegerField(required=True)
    min_days = forms.IntegerField(required=True)
    max_days = forms.IntegerField(required=True)

    def clean(self):
        return self.cleaned_data



