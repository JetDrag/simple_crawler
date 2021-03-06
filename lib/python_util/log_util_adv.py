# coding=utf8
__author__ = 'wangjunhao<wangjunhao@conew.com>'

import logging

# 单例模式装饰器，确保不重复添加handler
def singleton(cls):
    instances = {}
    def _singleton(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return _singleton


@singleton
class LogHelper():

    def __init__(self, log_file_name, logger, level):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_file_name,encoding='utf-8')
        fh.setLevel(level)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

class LogHelperForDBConnect():

    def __init__(self, log_file_name, logger, level):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_file_name,encoding='utf-8')
        fh.setLevel(level)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s')
        fh.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger