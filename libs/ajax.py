#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: ajax.py
@time: 2017/4/25 16:40
"""

import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def ajax_data(data):
    """
    返回json数据
    """
    data = simplejson.dumps(data)
    return HttpResponse(data, content_type="application/json")

def ajax_template(request, html_path, data):
    """
    返回渲染页面
    """
    t = loader.get_template(html_path)
    s = t.render(data, request)
    return HttpResponse(s)

def go_url(url):
    """
    url跳转
    """
    return HttpResponseRedirect(url)