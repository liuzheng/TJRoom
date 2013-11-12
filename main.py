#!/usr/bin/env python
# coding: utf-8
#  
# Copyright (c) 2013 
# Gmail:liuzheng712
#

import requests
import re
import urllib
import json
import webbrowser
import getpass

username = raw_input("input the UserName: ").strip()
password = getpass.getpass("input the PassWord: ")
url_login = 'http://tjis.tongji.edu.cn:58080/amserver/UI/Login'
session = requests.Session()
resp = session.get(url_login)

FormData = {
    'IDToken0': '',
    'IDToken1': username,
    'IDToken2': password,
    'IDButton': 'Log In',
    'goto': 'http://zcc.tongji.edu.cn/index.portal',
    'gx_charset':'UTF-8'
    }
resp = session.post(url_login, data=FormData)
#print "UserName:" + username + "\nPassWord:" + password
print re.findall('cg\.gif',resp.content)

room = session.get('http://zcc.tongji.edu.cn/detach.portal?.pa=aT1QMzM4ODE4JnQ9YSZzPW1heGltaXplZCZtPXZpZXc%3D&act=showBaseInfo')
print room.content
#webbrowser.open('http://zcc.tongji.edu.cn/detach.portal?.pa=aT1QMzM4ODE4JnQ9YSZzPW1heGltaXplZCZtPXZpZXc%3D&act=showBaseInfo',)
