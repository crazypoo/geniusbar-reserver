# -*- coding: utf-8 -*-
from utils.webpage import WebPage
import subprocess
import re
from multiprocessing import Pool
import multiprocessing
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
        portpattern = '(80){1,2}'
        isIp = False
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


def Checker(ip, processData):
    cmd = 'ping -n 2 -w 2 %s' % ip

    processData['curIndex'] += 1
    result = None
    try:
        res = subprocess.check_output(cmd)
        if not -1 == res.find('TTL='):
            debug.debug('find %s' % ip)
            result = ip
    except Exception as e:
        debug.debug(str(e))
    finally:
        debug.debug(cmd)
        index = processData['curIndex']
        total = processData['total']
        processData['progress'] = (index*100 / total)
        return result


class ProxyFinder():
    def __init__(self, urls):
        self.urls = urls

    def get_available_proxys(self, procData):
        restips = []
        for url in self.urls:
            tmppage = ProxyPage(url)
            ips = tmppage.get_proxyservers()
            pool = Pool(processes=multiprocessing.cpu_count()*2)
            procData['total'] = len(ips)
            procData['curIndex'] = 5
            for ip, port in ips:
                res = pool.apply_async(Checker, (ip, procData))
                if res.get():
                    restips.append((ip, port))
                    if len(restips) == 10:
                        break
            pool.close()
            pool.join()
        newips = {}.fromkeys(restips).keys()
        with open('res/proxyservers.dat', 'w') as f:
            for ip, port in newips:
                f.write('%s:%s\n' % (ip, port))
        return newips

    def getAvaliable(self, proxyServers, procData):
        restips = []
        pool = Pool(processes=multiprocessing.cpu_count()*2)
        for ip, port in proxyServers:
            res = pool.apply_async(Checker, (ip, procData))
            if res.get():
                restips.append((ip, port))
                pool.close()
                pool.join()
                newips = {}.fromkeys(restips).keys()
        return newips

