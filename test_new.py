import gevent.monkey
gevent.monkey.patch_socket()

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
    r = requests.Request('http://www.baidu.com')
    print r.
    print pid

@timeit_deco
def synchronous():
    for i in range(1,50):
        fetch(i)

@timeit_deco
def asynchronous():
    threads = []
    for i in range(1,50):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()