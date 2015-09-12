# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from configs_and_constants import Configs
from transaction_util import get_logger
from python_util.traceback_log import print_except_trace

import requests
from gevent import socket

# 模块单例性，确保同一站点统一session
s = requests.session()
logger = get_logger()


class Spider(object):

    def __init__(self,url,headers = Configs.HEADERS):
        self.url = url
        self.headers = headers
        logger.debug('Spider is fetching %s .' % self.url)

    def response(self):
        try :
            n = 0
            while n < 3:
                r = s.get(self.url,headers = self.headers,timeout= 10)
                if r.status_code == requests.codes.ok:
                    return r
                else:
                    logger.warning('Fetching Fail. The status code is %s. %s' % (r.status_code,self.url))
                n += 1
            return None
        except requests.Timeout or socket.timeout:
            logger.warning('Fetching Fail. Time out. %s' % self.url)
        except:
            logger.error(print_except_trace())