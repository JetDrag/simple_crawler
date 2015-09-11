# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from python_util.db_helper import MySqlHelper
from configs_and_constants import Configs,Contants

class DataAccess(object):

    def __init__(self):
        self.db_local = MySqlHelper(Contants.CLEAN_MASTER_RESOURCE_IP, Contants.CLEAN_MASTER_RESOURCE_PORT,
                                    Contants.CLEAN_MASTER_RESOURCE_DB, Contants.CLEAN_MASTER_RESOURCE_USER, Contants.CLEAN_MASTER_RESOURCE_PASS)