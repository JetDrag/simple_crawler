# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from python_util.db_helper import MySqlHelper
from configs_and_constants import Contants
from transaction_util import get_logger

logger = get_logger()

class DataAccess(object):

    def __init__(self):
        self.db_local = MySqlHelper(Contants.CACHE_IP, Contants.CACHE_PORT,
                                    Contants.CACHE_DB, Contants.CACHE_USER, Contants.CACHE_PASS)

    def store_data(self,save_task_lst):
        try:
            sql = 'INSERT INTO crawler_save (web_content,url) VALUES (%s,%s)'
            ret = self.db_local.ExecuteSql(sql,save_task_lst,many = True,commit= True)
            logger.info('Saved web content count is %s/%s.' % (str(ret[0]),str(len(save_task_lst))))
        except:
            logger.warning('Saving web content Fail! CNT is %s ' % str(len(save_task_lst)))