#!C:\Python27\python.exe
#-*- coding:utf-8 -*-
'''
Created on 2011-12-7

@author: ZouYipeng <ZouYipeng@Kingsoft.com>
@auther: modified by wangjunhao<wangjunhao@conew.com>
'''
import sys
import traceback
from log_util import get_logger

Logger = get_logger()
def print_except_trace():
    info = sys.exc_info()
    logs = []
    logs.append('[EXCEPTION]Traceback as below:')
    for fname, lineno, function, text in traceback.extract_tb(info[2]):
        logs.append('%s line %s in %s()' % (fname, lineno, function))
        logs.append('  => %s' % repr(text))
        logs.append('  ** %s: %s' % info[:2])

    Logger.error('\n'.join(item for item in logs))