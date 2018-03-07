# -*- coding:utf-8 -*-
__author__ = 'orange'
__date__ = '2017/9/20 上午11:51'

from url import *
import os

import tornado.web

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="
)

application = tornado.web.Application(
    handlers=url,
    **settings
)