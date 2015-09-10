# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from bs4 import BeautifulSoup
import urlparse

class Crawler(object):

    def __init__(self,response,url):
        self.soup = BeautifulSoup(response.content,'lxml')
        self.url = url

    def lookup_condition(self,tag):
        return tag.name == 'a' and tag.has_attr('href')

    def new_resource(self):
        new_resource_set = set()
        for item in self.soup.find_all(self.lookup_condition):
            end_url = urlparse.urljoin(self.url,item.attrs.get("href"))
            if end_url.startswith(self.url):
                filtered_url = end_url.split('#')[0]
                new_resource_set.add(filtered_url)
        return new_resource_set

    def original_new_resource(self):
        for item in self.soup.find_all('a'):
            print item.attrs.get('href')