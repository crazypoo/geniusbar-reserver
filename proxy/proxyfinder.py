# -*- coding: utf-8 -*-
from utils.webpage import WebPage


class ProxyPage(WebPage):
    def __init__(self, url,
                 data=None,
                 headers={},
                 charset='utf-8',
                 timeout=100):
        super(ProxyPage, self).__init__(url, data,
                                        headers,
                                        charset,
                                        timeout)


class ProxyFinder():
    def __init__(self, urls):
        self.urls = urls

    def getAvailableProxyIp(self):
        pass
