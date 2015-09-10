# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from run import run_prepare
from lib import fetcher

run_prepare()

print fetcher.Fetcher('http://www.python-requests.org/en/latest/user/advanced/').start()