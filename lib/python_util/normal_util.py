# coding=utf8
__author__ = 'wangjunhao<wangjunhao@conew.com>'

import re

class CodecsTools(object):

    @staticmethod
    def encode_utf8_in_lst(lst):
        new_lst = []
        for item in lst:
            new_lst.append(item.encode('utf8'))
        return new_lst

class DictionaryTools(object):

    @staticmethod
    def list_to_dct(lst):
        dct = {}
        for i in lst:
            dct[i] = ''
        return dct

class CheckSumTools(object):

    @staticmethod
    def re_pattern_find(content_re,content):
        tag = 0
        pattern = re.compile(content_re + '$')
        buf = pattern.findall(content)
        if len(buf) > 0:
            tag = 1
        return tag