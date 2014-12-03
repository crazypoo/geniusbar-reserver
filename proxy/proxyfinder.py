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

    def get_proxyservers(self):
        servers = []
        soup = self.get_soup()
        return servers


class ProxyFinder():
    def __init__(self, urls):
        self.urls = urls


    def get_available_proxys(self):
        ips = []
        return ips
