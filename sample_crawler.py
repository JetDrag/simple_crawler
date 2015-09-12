# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from gevent import pool,queue
import base64,time

from lib.configs_and_constants import Configs
from lib.transaction_util import get_logger
from lib.crawler import Crawler
from lib.spider import Spider
from lib.data_access import DataAccess

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
        self.key_word = Configs.KEYWORD
        self.benchmark = Configs.BENCHMARK
        self.delay_time = Configs.DELAY_TIME


    # 在协程中实现关键词过滤; 网页和网址转化成安全base64编码,扔入存储队列。
    def single_simple_crawler(self,new_url):
        response = Spider(new_url).response()
        if response:
            if not self.benchmark:
                if not self.key_word or (self.key_word and self.key_word in new_url):
                    self.save_queue.put((base64.urlsafe_b64encode(response.content),base64.urlsafe_b64encode(new_url)))
            for item in Crawler(response).new_resource():
                self.url_queue.put(item)

    def single_save_process(self,save_task_lst):
        DataAccess().store_data(save_task_lst)


    def simple_crawler_main(self):

        # 将初始任务扔到队列里，新建协程池
        self.url_queue.put(Configs.URL)
        crawler_pool = pool.Pool(100)
        save_pool = pool.Pool(10)
        exist_url_set = set()

        while self.now_cnt < self.limit_cnt and not self.url_queue.empty():

            # 爬取操作和队列维护;1,为深度优先;2,为广度优先;使用协程异步爬取任务。
            url_set = set()
            while not self.url_queue.empty():
                url_set.add(self.url_queue.get())
            if url_set:
                if self.priority == 1:
                    url_task_list = sorted(url_set.difference(exist_url_set),key = lambda x:len(x),reverse = True)
                elif self.priority == 2:
                    url_task_list = sorted(url_set.difference(exist_url_set),key = lambda x:len(x))

                if self.now_cnt + len(url_task_list) > self.limit_cnt:
                    url_task_list = url_task_list[:(self.limit_cnt - self.now_cnt)]

                # 下发任务的时候暂停指定时间
                for new_url in url_task_list:
                    time.sleep(self.delay_time)
                    crawler_pool.apply_async(self.single_simple_crawler,(new_url,))

                logger.info('Applied %s tasks to gevent pool' % len(url_task_list))
                # 抓取池阻塞
                crawler_pool.join()

                # 计数与去重维护
                exist_url_set.update(url_set)
                self.now_cnt += len(url_task_list)
                logger.info('Now the count of crawlered web is %s.' % str(self.now_cnt))

            if not self.benchmark:
                # 存储操作和队列维护;使用协程异步存储至mysql。
                save_task_lst = []
                while not self.save_queue.empty():
                    content,new_url = self.save_queue.get()
                    save_task_lst.append((content,new_url))
                logger.info('Creating a new greenlet to save web page to MySQL.')
                if save_task_lst:
                    save_pool.apply_async(self.single_save_process,(save_task_lst,))

        logger.info('Crawl finished ! Wait for data saving finished !')

        # 存储池在爬取结束后阻塞，等待结束
        save_pool.join()
        logger.info('Data saving finished !')