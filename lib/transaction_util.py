# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from python_util import log_util_adv,traceback_log
from configs_and_constants import Configs,Contants

# TODO:将统一get_logger移至下层或log_util中，方便底层工具调用
def get_logger():
    logger = log_util_adv.LogHelper(Configs.LOGFILE ,Contants.DEFAULT_LOGGER,Configs.LOGLEVEL).getlog()
    return logger
