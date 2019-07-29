#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: urls.py
@time: 2019/7/29 10:07
"""
import time
from dwebsocket.decorators import accept_websocket, require_websocket

from libs import ajax


def r_html(request):
    return ajax.ajax_template(request, 'websocket/index.html', {})

@accept_websocket
def test(request):
    if request.is_websocket():
        while 1:
            msg = request.websocket.read()
            if msg:
                msg = msg.decode()
                res = "hello" + msg
                request.websocket.send(res.encode("utf-8"))
                if msg == "5":
                    request.websocket.close()
                    break