# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from utils import debug
debug.setLevel(10)
from gui import interface
# init proxy servers
from proxy.proxyfinder import ProxyFinder
from multiprocessing import freeze_support
freeze_support()
urls = ['http://www.proxy360.cn/Region/China']
        #'http://www.3464.com/data/Proxy/Http/']


def InitProxyServers():
    proxyFinder = ProxyFinder(urls)
    ips = proxyFinder.get_available_proxys()
    with open('avalibeips.txt','w') as f:
        for ip ,port in ips:
            f.write('ip:%s\n' % (ip, port))
    return ips


if __name__ == '__main__':
    interface.main()
