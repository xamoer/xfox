#!/usr/bin/env python
# coding:utf-8

"""
Created by ben on 2010/8/7 .
Copyright (c) 2010 http://sa3.org All rights reserved. 
"""

import datetime
from google.appengine.ext import webapp
register = webapp.template.create_template_register()

def datetz(value,arg):
    t = datetime.timedelta(seconds=3600*8) #8hour
    return webapp.template.django.template.defaultfilters.date(value+t, arg)

register.filter(datetz)

def humdate(value):
    tmp = datetime.datetime.now() -value
    if tmp.days > 0:
        return datetz("M d,Y H:i")
    if tmp.seconds < 60:
        return u"%s 秒前" % tmp.seconds
    if tmp.seconds <3600:
        return u"约%s分钟前" % (tmp.seconds/60)
    return u"约%s小时前" % (tmp.seconds/3600)

register.filter(humdate)

if __name__=='__main__':
    pass