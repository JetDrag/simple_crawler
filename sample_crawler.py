# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

import gevent.monkey
gevent.monkey.patch_all()

import gevent,os

from lib.configs_and_constants import Configs,Contants
from lib.transaction_util import get_logger
from lib.crawler import Crawler
from lib.fetcher import Fetcher

class Simple_Crawler(object):
    '''
    Todo:尝试使用属性方法优化代码可读性
    '''
    def __init__(self):
        self.url_queue = gevent.queue.Queue()
        self.save_queue = gevent.queue.Queue()
        self.key_word = Configs.KEYWORD
        self.result_dir = '/'.join(['result_data',Configs.URL])
        self.limit_cnt = Configs.LIMIT
        self.now_cnt  = 0


    def single_simple_crawler(self,new_url):
        response = Fetcher(new_url).response()
        if response:
            if not self.key_word or (self.key_word and self.key_word in new_url):
                self.save_queue.put(response.content)
            for item in Crawler(response).new_resource():
                self.url_queue.put(item)


    def simple_crawler_main(self):
        if not os.path.exists(self.result_dir):
            os.makedirs(self.result_dir)

        self.url_queue.put(Configs.URL)
        pool = gevent.pool(50)
        


        while self.now_cnt < self.limit_cnt and not self.url_queue.empty():




