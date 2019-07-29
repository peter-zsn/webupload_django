#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: urls.py
@time: 2019/7/29 10:07
"""

from django.conf.urls import include, url
from apps.websock import views


urlpatterns = [
    url(r'^html/$', views.r_html),             # 测试
    url(r'^test/$', views.test),             # 测试
]
