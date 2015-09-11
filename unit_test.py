# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from run import run_prepare
from lib import spider

run_prepare()

print spider.Spider('http://www.python-requests.org/en/latest/user/advanced/').start()