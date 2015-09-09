# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from lib.configs_and_constant import Contants,Configs
from lib import transaction_util
import argparse,random

def main():
    # 参数处理
    parse = argparse.ArgumentParser(description= 'An Simple Crawler!')

    parse.add_argument('url',
                       help = 'Input the url you want to crawler.')

    parse.add_argument('-hd','--header', default = random.choice(Contants.USER_AGENTS),
                       help = 'Specify your header for your crawler.')

    parse.add_argument('-d','--depth', default = 1000, type = int,
                       help = 'Specify depth for your crawler.')

    parse.add_argument('-t','--delay_time', default = 1, type = int,
                       help = 'Specify delay time for your crawler.')

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
    Configs.url = args.url
    Configs.header = args.header
    Configs.depth = args.depth
    Configs.delay_time = args.delay_time
    Configs.priority = args.priority
    Configs.limit = args.limit
    Configs.keyword = args.keyword
    Configs.logfile = args.logfile
    Configs.loglevel = args.loglevel


    # 爬取开始
    logger = transaction_util.get_logger()


    logger.info(u'开始爬取%s.'% Configs.url)
