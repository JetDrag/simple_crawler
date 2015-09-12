# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from lib.configs_and_constants import Configs,Contants

Configs.HEADERS = {'user-agent':Contants.USER_AGENTS[1]}
Configs.DEPTH = 2
Configs.URL = 'http://www.wooyun.org/'
Configs.LOGFILE = 'xx.log'
Configs.LOGLEVEL = 10

import unittest
from lib.spider import Spider
from lib.crawler import Crawler



class test_for_simple_crawler(unittest.TestCase):

    def setUp(self):
        self.url = Configs.URL

    def test_site_filter(self):
        for item in Crawler(Spider(self.url).response()).new_resource():
            self.assertTrue(item.startswith(self.url))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()