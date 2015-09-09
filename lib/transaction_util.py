# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from python_util import log_util_adv
from configs_and_constant import Configs,Contants

def get_logger():
    logger = log_util_adv.LogHelper(Configs.logfile,Contants.DEFAULT_LOGGER,Configs.loglevel).getlog()
    return logger