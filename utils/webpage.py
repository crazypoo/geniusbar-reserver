import re
import urllib2
import cookielib
from utils import debug
from BeautifulSoup import BeautifulSoup


class WebPage(object):
    cookie = None
    opener = None

    def __init__(self, url,
                 data=None,
                 headers={},
                 charset="utf-8",
                 timeout=20):

        self.url = url
        self.timeout = timeout
        self.charset = charset
        self.headers = headers
        self.post_data = data
        self.data = None
        self.soup = None

    def reOpen(self):
        self.data = None
        self.soup = None

    def get_url(self):
        return self.url

    def get_headers(self):
        return self.headers

    def _read_page(self):
        # self.init_cookie()
        if self.post_data:
            debug.debug('post %s' % self.url)
        else:
            debug.debug('read %s' % self.url)
        req = urllib2.Request(self.url,
                              data=self.post_data,
                              headers=self.headers)
        counter = 3
        while counter > 0:
            try:
                res = urllib2.urlopen(req, data=None, timeout=self.timeout)
                data = res.read()
                return data
            except Exception as e:
                debug.info(str(e))
                counter -= 1
        debug.error('Read failed')
        return None

    def get_charset(self, html):
        r = '\w*charset=(".*").*'
        r = re.compile(r)
        m = r.match(html)
        if m:
            print(m.group(1))
            self.charset = m.group(1)
        else:
            print(html.find('charset='))
            print("not found")

    def init_cookie(self):
        if WebPage.cookie:
            return
        debug.info('do init cookie')

        WebPage.cookie = cookielib.LWPCookieJar('tmpcookie')
        cookie_support = urllib2.HTTPCookieProcessor(WebPage.cookie)
        WebPage.opener = urllib2.build_opener(cookie_support)
        urllib2.install_opener(WebPage.opener)

    def get_data(self):
        if self.data:
            return self.data

        html = self._read_page()
        self.data = self.encode_page_data(html)
        return self.data

    def encode_page_data(self, data):
        # find charset

        if 'utf-8' == self.charset:
            data = data.decode(self.charset, 'ignore').replace('&nbsp', '')
        else:
            data = data.decode('GBK', 'ignore').replace('&nbsp', '')
            data = data.encode('utf-8')

        return data

    def get_page(self, data=None):
        if not data:
            html = self._read_page()
            data = self.encode_page_data(html)
        self.soup = BeautifulSoup(markup=data)
        return self.soup

    def get_soup(self, data=None):
        if data:
            self.soup = BeautifulSoup(markup=data)
            return self.soup
        if self.soup:
            return self.soup
        self.soup = BeautifulSoup(markup=self.get_data())
        return self.soup

    def get_tag_value(self, tagLabel, attrs):
        soup = self.get_soup()
        try:
            tag = soup.find(tagLabel, attrs=attrs)
            return tag.get('value')
        except AttributeError as e:
            debug.info('info cannot find %s %s' % (tagLabel, str(e)))
            return ''

    def get_tag_text(self, taglabel, attrs):
        soup = self.get_soup()
        try:
            tag = soup.find(taglabel, attrs=attrs)
            return tag.text
        except AttributeError as e:
            debug.error('cannot find %s %s %s' %
                        (taglabel, str(attrs), str(e)))
            return None

    def get_tags(self, tagLabel, attrs):
        soup = self.get_soup()
        return soup.findAll(tagLabel, attrs=attrs)
