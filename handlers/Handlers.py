#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import tornado.web as web
import tornado.escape as escape
import tornado.gen as gen

logged_sessions = dict() # global var
db_access = {'username': 'root',
             'password': '@LIU3226677zc!',
             'dbname': 'Shanghai_Data'}

class BaseHandler(web.RequestHandler):
    def get_current_user(self): # for attr self.current_user
        session = self.get_secure_cookie('session')
        return logged_sessions.get(session, None) # what should be the default?

class IndexHandler(BaseHandler):

    def get(self):
        self.render('index.html')

















