# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

from bs4 import BeautifulSoup
import re,requests

headers = {'user-agent': 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko'}
html_doc_obj = requests.get('http://www.python-requests.org/en/latest/user/quickstart/',headers = headers)


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc_obj.text,'lxml')


for i in  soup.html.find_all('a'):
    print '________'
    print i