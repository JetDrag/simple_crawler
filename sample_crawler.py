# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

import gevent.monkey
gevent.monkey.patch_all()

from gevent import pool,queue
import os

from lib.configs_and_constants import Configs,Contants
from lib.transaction_util import get_logger
from lib.crawler import Crawler
from lib.spider import Spider

logger = get_logger()


class Simple_Crawler(object):
    '''
    Todo:尝试使用属性方法优化代码可读性
    '''
    def __init__(self):
        self.url_queue = queue.Queue() # 爬取队列
        self.save_queue = queue.Queue() # 存储队列
        self.limit_cnt = Configs.LIMIT
        self.now_cnt  = 0
        self.priority = Configs.PRIORITY

    # 在协程中实现关键词过滤
    def single_simple_crawler(self,new_url):
        response = Spider(new_url).response()
        if response:
            if not self.key_word or (self.key_word and self.key_word in new_url):
                self.save_queue.put((response.content,new_url))
            for item in Crawler(response).new_resource():
                self.url_queue.put(item)


    def simple_crawler_main(self):

        # 将初始任务扔到队列里，新建协程池
        self.url_queue.put(Configs.URL)
        crawler_pool = pool.Pool(50)
        exist_url_set = set()

        while self.now_cnt < self.limit_cnt and not self.url_queue.empty():

            # 爬取操作和队列维护
            url_set = set()
            while not self.url_queue.empty():
                url_set.add(self.url_queue.get())
            if url_set:
                if self.priority == 1:
                    url_task_list = sorted(url_set.difference(exist_url_set),key = lambda x:len(x),reverse = True)
                elif self.priority == 2:
                    url_task_list = sorted(url_set.difference(exist_url_set),key = lambda x:len(x))
                for new_url in url_task_list:
                    crawler_pool.apply_async(self.single_simple_crawler,(new_url,))

                crawler_pool.join()

            # 存储操作和队列维护
            save_task_lst = []
            while not self.save_queue.empty():
                save_task_lst.append(self.save_queue.get())
                # Todo:Mysql存储
            print save_task_lst






