#!C:\Python27\python.exe
#-*- coding:utf-8 -*-
'''
@auther: modified by wangjunhao<wangjunhao@conew.com>
'''
import sys
import traceback

def print_except_trace():
    info = sys.exc_info()
    logs = []
    logs.append('[EXCEPTION]Traceback as below:')
    for fname, lineno, function, text in traceback.extract_tb(info[2]):
        logs.append('%s line %s in %s()' % (fname, lineno, function))
        logs.append('  => %s' % repr(text))
        logs.append('  ** %s: %s' % info[:2])

    return ('\n'.join(item for item in logs))
