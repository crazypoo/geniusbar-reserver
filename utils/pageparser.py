# -*- coding: utf-8 -*-
import sys
import urllib.request as request
from bs4 import BeautifulSoup
from utils import debug


class PageParser(object):
    def __init__(self, pageurl):
        self.pageUrl = pageurl
        self.soup = None
        self.data = None

    def _findItemByAttrs(self, attrs):
        soup = self.getSoup()
        item = soup.find('input', attrs=attrs)
        return item

    def getData(self):
        print('getData')
        if self.data:
            return self.data
        counter = 3
        while counter > 0:
            try:
                response = request.urlopen(self.pageUrl)
                debug.output('parsing %s' % self.pageUrl)
                html = response.read()
                data = html.decode('utf-8', 'ignore').replace('&nbsp', '')
                data = data.encode('utf-8')
                return data
            except Exception as e:
                debug.error('%s %s will retry again' % (self.pageUrl, str(e)))
                counter -= 1

    def _getSoup(self):
        print("__getSoup")
        counter = 3
        while counter > 0:
            try:
                response = request.urlopen(self.pageUrl)
                html = response.read()
                data = html.replace('&nbsp', '')
                # data = html.decode('gbk', 'ignore').replace('&nbsp', '')
                # print('data')
                # data = data.encode('utf-8')
                self.data = data
                self.soup = BeautifulSoup(markup=data)
                return self.soup
            except Exception as e:
                debug.error('%s %s will retry again' % (self.pageUrl, str(e)))
                counter -= 1

    def getSoup(self):
        if self.soup:
            return self.soup
        self.soup = self._getSoup()
        return self.soup
