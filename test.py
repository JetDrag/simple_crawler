# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

import requests,traceback

try:
    i = requests.get('http://www.121888.com',timeout =0.001)
except:
    print traceback.print_exc()