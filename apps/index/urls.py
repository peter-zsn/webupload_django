#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: urls.py
@time: 2017/4/25 16:36
"""

from django.conf.urls import include, url
from apps.index import views

urlpatterns = [
    url(r'^api/', views.p_api),                 # 返回接口数据
    url(r'^api_html/', views.p_html),                 # 返回页面渲染
    url(r'^upload/', views.upload),                 # 分片上传---先传到服务器内存，在进行分片写入服务器文件
]
