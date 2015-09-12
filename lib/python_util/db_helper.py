#-*- coding:utf8 -*-
__author__ = 'Wang'

import pymysql as MySQLdb
# import MySQLdb
import sqlite3,sys
import traceback_log,log_util_adv

# TODO:将统一get_logger移至下层或log_util中，方便底层工具调用
def get_logger():
    logger = log_util_adv.LogHelperForDBConnect('log/' + __name__ ,__name__,10).getlog()
    return logger
logger = get_logger()

class SQLiteHelper(object):
    def __init__(self,db,):
        self.db = db
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db)

    def execute_sql(self, sql, params, many = False, script = False):
        if not self.conn:
            self.connect()

        ret = 0
        try:
            with self.conn:
                if many:
                    ret = self.conn.executemany(sql,params)
                elif script:
                    ret = self.conn.executescript(sql)
                else:
                    ret = self.conn.execute(sql,params)
        except:
            print sys.exc_info()[0],sys.exc_info()[1]
            print sql

        return ret


class MySqlHelper():
    def __init__(self, ip, port, db, usr, psw):
        self.db = None
        self.db_cfg = [ip,port , db, usr, psw]

    def Connect(self):
        ''' Connect to remote database
        '''
        ret = 0
        try:
            self.db = MySQLdb.Connect(host = self.db_cfg[0],
                                        port = self.db_cfg[1],
                                        db = self.db_cfg[2],
                                        user = self.db_cfg[3],
                                        passwd = self.db_cfg[4],
                                        charset='utf8')
            ret = 1
        except:
            print traceback_log.print_except_trace()
        return ret

    def CloseDB(self):
        '''Close database Connection
        '''
        if self.db != None:
            self.db.close()
            self.db = None


    def ExecuteSql(self, sql, params, many=False, commit=False):
        '''Execute sql.
        many: insert or update or delete by muti-conditions.
              used ONLY when need change data (insert, update, delete)
        commit: used ONLY when need change data (insert, update, delete)
        '''
        ret = 0
        cds = ()
        bConnected = False
        # 1. 确认连接是否成功
        if self.db == None:
            bConnected = self.Connect()
        else:
            try:
                self.db.ping()
                bConnected = True
            except MySQLdb.OperationalError:
                if self.db == self.db:
                    self.Connect()
                    self.db = self.db
            except Exception:
                print traceback_log.print_except_trace()
        try:
            cursor = self.db.cursor()
            if many:
                ret = cursor.executemany(sql, params)
            else:
                ret = cursor.execute(sql, params)
            if commit:
                self.db.commit()
            else:
                cds = cursor.fetchall()
            cursor.close()
        except Exception, ex:
            tip_str = '[Exec sql exception] %s' % str(ex)
            print tip_str
            logger.info('\n'.join([tip_str,sql,repr(params[0])]))
            if commit:
                self.db.rollback()
        return ret, cds
