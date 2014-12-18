import urllib2
import cookielib
proxyserver = '221.7.112.108:80'
url = 'http://www.baidu.com'
#proxyserver = '120.137.170.199:80'
def build_opener(proxyServer=None):
     
    cookie = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cookie)
    if proxyServer:
         
        proxyHandler = urllib2.ProxyHandler({'http': proxyServer})
        opener = urllib2.build_opener(proxyHandler,
                                      cookie_support,
                                      urllib2.HTTPHandler)
    else:
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
 
def proxy2():
    build_opener(proxyserver)
    content = urllib2.urlopen(url)
    print(content.read())
def proxy1():
    proxy = proxyserver
    proxyHandler = urllib2.ProxyHandler({'http': proxy})
    opener = urllib2.build_opener(proxyHandler)
    urllib2.install_opener(opener)
    print('open %s' % url)
    content = urllib2.urlopen(url)
    print(content.read())

proxy2()
