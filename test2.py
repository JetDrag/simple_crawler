# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

import gevent

def print_info():
    gevent.sleep(5)
    print a

a = ['2','3']
l = [gevent.spawn(print_info)]

a = ['3','4']
l.append(gevent.spawn(print_info))

gevent.joinall(l)