# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from lib.configs_and_constants import Contants,Configs
from lib import transaction_util
import argparse,random

def run_prepare():
    # 参数处理
    parse = argparse.ArgumentParser(description= 'An Simple Crawler!')

    parse.add_argument('url',
                       help = 'Input the url you want to crawler.')

    parse.add_argument('-hd','--headers', default = random.choice(Contants.USER_AGENTS),
                       help = 'Specify your header for your crawler.')

    parse.add_argument('-d','--depth', default = 2, type = int,
                       help = 'Specify depth for your crawler.')

    parse.add_argument('-t','--delay_time', default = 0, type = int,
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

    parse.add_argument('-ll','--loglevel', default = 10,
                       help = 'Specify logger level.')

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

    # 参数获取完毕
    logger = transaction_util.get_logger()
    logger.info(u'Gotten arguments. Crawling %s.'% Configs.URL)

if __name__ == '__main__':
    run_prepare()


