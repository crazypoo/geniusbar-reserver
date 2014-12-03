import urllib2
proxyserver = '221.7.112.108:80'
url = 'http://www.baidu.com'
#proxyserver = '120.137.170.199:80'


def proxy1():
    proxy = proxyserver
    proxyHandler = urllib2.ProxyHandler({'http': proxy})
    opener = urllib2.build_opener(proxyHandler)
    urllib2.install_opener(opener)
    print('open %s' % url)
    content = urllib2.urlopen(url)
    print(content.read())

proxy1()
