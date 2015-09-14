# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

import gevent.monkey
gevent.monkey.patch_all()

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from lib.configs_and_constants import Contants,Configs
from lib import transaction_util
import argparse

def run_prepare():
    # 参数处理
    parse = argparse.ArgumentParser(description= 'An Simple Crawler!')

    parse.add_argument('url',
                       help = 'Input the url you want to crawler.')

    parse.add_argument('-hd','--headers', default = Contants.USER_AGENTS[1],
                       help = 'Specify your header for your crawler.')

    parse.add_argument('-d','--depth', default = 2, type = int,
                       help = 'Specify depth for your crawler.')

    parse.add_argument('-t','--delay_time', default = 0, type = float,
                       help = 'Specify delay time for your crawler.')

    # 1为深度优先，2为广度优先
    parse.add_argument('-p','--priority', default = 1, choices = [1,2], type = int,
                       help = 'Specify strategy for your crawler.')

    parse.add_argument('-l','--limit', default = 1000, type = int,
                       help = 'Specify page limit count of pages.')

    parse.add_argument('-k','--keyword', default = None,
                       help = 'Specify keyword for your crawler.')

    parse.add_argument('-lf','--logfile', default = Contants.DEFAULT_LOG_FILE_NAME,
                       help = 'Specify logfile location.')

    parse.add_argument('-ll','--loglevel', default = 10, choices = [0, 10, 20, 30, 40, 50],type = int,
                       help = 'Specify logger level.')

    parse.add_argument('-b','--benchmark', default = 0, choices = [0,1], type = int,
                       help = 'Disable data store process to benchmark crawler speed.')

    args = parse.parse_args()


    # 参数存储
    Configs.URL = args.url
    Configs.HEADERS = {'user-agent':args.headers}
    Configs.DEPTH = args.depth
    Configs.DELAY_TIME = args.delay_time
    Configs.PRIORITY= args.priority
    Configs.LIMIT = args.limit
    Configs.KEYWORD = args.keyword
    Configs.LOGFILE = args.logfile
    Configs.LOGLEVEL = args.loglevel
    Configs.BENCHMARK = args.benchmark


    # 参数获取完毕
    logger = transaction_util.get_logger()
    logger.info('Gotten arguments. Crawling %s.'% Configs.URL)

if __name__ == '__main__':
    run_prepare()
    # Simple_Crawler中import的模块需要的参数需要run_prepare初始化
    from sample_crawler import Simple_Crawler
    Simple_Crawler().simple_crawler_main()
