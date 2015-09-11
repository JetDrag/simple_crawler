# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from bs4 import BeautifulSoup
import urlparse
from configs_and_constants import Configs

class Crawler(object):

    # response 是 request 返回的对象, url为归属的站点
    def __init__(self,response,site_url = Configs.URL):
        self.soup = BeautifulSoup(response.content,'lxml')
        self.site_url = site_url
        self.depth = Configs.DEPTH
        self.site_url_depth = len(site_url.split('/'))

    # 过滤出<a href=>标签
    def lookup_condition(self,tag):
        return tag.name == 'a' and tag.has_attr('href')

    # 过滤归属站点，过滤深度，过滤#符
    def new_resource(self):
        new_resource_set = set()
        for item in self.soup.find_all(self.lookup_condition):
            end_url = urlparse.urljoin(self.site_url,item.attrs.get("href"))
            if end_url.startswith(self.site_url) and end_url.split('/') - self.site_url_depth <= 3:
                filtered_url = end_url.split('#')[0]
                new_resource_set.add(filtered_url)
        return new_resource_set

    def original_new_resource(self):
        for item in self.soup.find_all('a'):
            print item.attrs.get('href')