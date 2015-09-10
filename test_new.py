# coding=utf8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import gevent.monkey
gevent.monkey.patch_all()

import gevent,time
import urllib2
import requests

def timeit_deco(func):
    def wrapper(*arg):
        start = time.time()
        func(*arg)
        end = time.time()
        print end - start
    return wrapper


def fetch(pid):
    r = requests.get('http://www.baidu.com')
    print pid

@timeit_deco
def synchronous():
    for i in range(1,500):
        fetch(i)

@timeit_deco
def asynchronous():
    threads = []
    for i in range(1,500):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()