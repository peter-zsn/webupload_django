#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: urls.py
@time: 2017/12/22 10:07
"""

from django.conf.urls import include, url, patterns
from apps.web import views                      # 文件形式的分片上传
from apps.web import rd_view                    # redis 形式的分片上传

# urlpatterns = [
#     url(r'^$', views.index),             # 一个分片上传后被调用
#     url(r'^success/$', views.upload_success),             # 所有分片上传成功后被调用
#     url(r'^file_exist/$', views.list_exist),             # 判断文件的分片是否存在
# ]


urlpatterns = [
    url(r'^$', rd_view.index),             # 一个分片上传后被调用
    url(r'^success/$', rd_view.upload_success),             # 所有分片上传成功后被调用
    url(r'^file_exist/$', rd_view.file_exist),             # 判断文件的是否存在
]
