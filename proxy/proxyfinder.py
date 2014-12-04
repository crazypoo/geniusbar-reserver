# -*- coding: utf-8 -*-
from utils.webpage import WebPage
import re, os
import subprocess
from multiprocessing import Pool, Queue
from utils import debug


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

    def get_proxyservers(self, port='80'):
        servers = []
        attrs = {'class': 'proxylistitem', "name": "list_proxy_ip"}
        tags = self.get_tags('div', attrs=attrs)
        ippattern = '(\d{2,3}\.){3}\d{1,3}'
        portpattern='(80){1,2}'
        isIp=False
        ip = None
        port = None
        for tag in tags:
            items = tag.findAll('span', attrs={'class': 'tbBottomLine'})
            for item in items:
                if not isIp:
                    m = re.match(ippattern, item.text)
                    if m:
                        isIp = True
                        ip = m.group(0)
                else:
                    isIp = False
                    m = re.match(portpattern, item.text)
                    if m:
                        port = m.group(0)
            if ip and port:
                servers.append((ip, port))
                ip = None
                port = None
        return servers


def Checker(ip):
    cmd = 'ping -n 2 -w 2 %s' % ip
    debug.debug(cmd)
    try:
        res = subprocess.check_output(cmd)
        if not -1 == res.find('TTL='):
            debug.debug('find %s' %ip)
            return ip
    except Exception as e:
        debug.debug(str(e))
        return False


class ProxyFinder():
    def __init__(self, urls):
        self.urls = urls

    def get_available_proxys(self):
        restips = []
        for url in self.urls:
            #tmppage = ProxyPage(url)
            #ips = tmppage.get_proxyservers()
            ips =[('219.131.198.100','80'), ('119.62.128.38', '80')]
            queue = Queue(len(ips))
            pool = Pool(processes=2)
            for ip, port in ips:
                res = pool.apply_async(Checker, (ip,))
                if res.get():
                    restips.append((ip, port))
            pool.close()
            pool.join()
        newips = {}.fromkeys(restips).keys()
        return newips
