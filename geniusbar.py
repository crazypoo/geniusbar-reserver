# -*- coding: utf-8 -*-
import sys
reload(sys)
import os
sys.setdefaultencoding('utf-8')
cwd = os.path.abspath(os.getcwd())
# sites
sys.path.append(os.path.join(cwd, 'gui'))
sys.path.append(os.path.join(cwd, 'proxy'))
sys.path.append(os.path.join(cwd, 'sites'))
sys.path.append(os.path.join(cwd, 'utils'))


from utils import debug
debug.setLevel(10)
from gui import interface
# init proxy servers
from proxy.proxyfinder import ProxyMgr
from multiprocessing import freeze_support
freeze_support()
urls = ['http://www.proxy360.cn/Region/China']
        #'http://www.3464.com/data/Proxy/Http/']


def InitProxyServers():
    proxyMgr = ProxyMgr(urls)
    ips = proxyMgr.getAvailableProxys()
    with open('avalibeips.txt','w') as f:
        for ip ,port in ips:
            f.write('ip:%s\n' % (ip, port))
    return ips


if __name__ == '__main__':
    interface.main()
