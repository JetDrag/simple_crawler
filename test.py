# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

import gevent.monkey
gevent.monkey.patch_all(subprocess=True,sys= True)

import gevent
from gevent import pool

def test(a):
    gevent.sleep(2)
    print a

test_pool = pool.Pool(50)

a_list = [1,2,3,4,5,6,7,8,9,10]

[test_pool.apply_async(test,(a,)) for a in a_list]

test_pool.join()