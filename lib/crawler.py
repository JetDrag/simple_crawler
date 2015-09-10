# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from bs4 import BeautifulSoup
import urlparse
from configs_and_constants import Configs

class Crawler(object):

    # response 是 request 返回的对象, url为归属的站点
    def __init__(self,response,url = Configs.URL):
        self.soup = BeautifulSoup(response.content,'lxml')
        self.url = url
        self.key_word = Configs.KEYWORD
        self.depth = Configs.DEPTH

    # 过滤出<a href=>标签
    def lookup_condition(self,tag):
        return tag.name == 'a' and tag.has_attr('href')

    # 过滤关键字，过滤归属站点，过滤深度，过滤#符
    # TODO: 过滤深度
    def new_resource(self):
        new_resource_set = set()
        for item in self.soup.find_all(self.lookup_condition):
            end_url = urlparse.urljoin(self.url,item.attrs.get("href"))
            if not self.key_word or self.key_word in end_url:
                if end_url.startswith(self.url):
                    filtered_url = end_url.split('#')[0]
                    new_resource_set.add(filtered_url)
        return new_resource_set

    def original_new_resource(self):
        for item in self.soup.find_all('a'):
            print item.attrs.get('href')