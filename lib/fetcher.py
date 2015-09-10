# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from configs_and_constants import Configs
from transaction_util import get_logger
from python_util.traceback_log import print_except_trace
import requests,time

s = requests.session()
logger = get_logger()

class Fetcher(object):

    def __init__(self,url,headers = Configs.HEADERS,delay_time = Configs.DELAY_TIME):
        time.sleep(delay_time)
        self.url = url
        self.headers = headers


    def response(self):
        try :
            n = 0
            while n < 3:
                r = s.get(self.url,headers = self.headers)
                if r.status_code == requests.codes.ok:
                    return r
                else:
                    logger.warn('Fetcher Fail. The status code is %s' % r.status_code)
                n += 1
            return ''
        except:
            logger.error(print_except_trace())