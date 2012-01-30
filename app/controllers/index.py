# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, db, urlfor, redirect

def index():
    template_response("/page/index.mako")

def testpage0():
    template_response("/error/notyet.mako")

def testpage1():
    template_response("/error/notyet.mako")

def testpage2():
    template_response("/error/notyet.mako")

def testpage3():
    template_response("/error/notyet.mako")
