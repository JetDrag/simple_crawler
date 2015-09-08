# coding=utf8
__author__ = 'wangjunhao<wangjunhao@conew.com>'

import sys,datetime,logging,os

# 单例模式装饰器，确保不重复添加handler
def singleton(cls):
    instances = {}
    def _singleton(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return _singleton

@singleton
class HelperLog():

    def __init__(self, logname, logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''

        # 创建一个logger

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname,encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

def get_logger():
    todayDate = datetime.datetime.now().strftime('%Y-%m-%d')
    PYName = sys.argv[0]
    PYName = PYName[PYName.rfind('/')+1:PYName.rfind('.')]
    if not os.path.exists('log'):
        os.makedirs('log')
    logger = HelperLog(logname='log/log_'+PYName+'_'+todayDate+'.txt', logger=PYName).getlog()
    return logger