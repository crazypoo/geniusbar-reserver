import sys
if '../' not in sys.path:
    sys.path.append('../')
#sys.path.append('../sites/apple_genius_bar/')
sys.path.append('../sites/')

from utils import webpage, Writefile, debug
import urllib2
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')
# debug
debug.setLevel(10)


def test_web_page():
    url = "http://store.apple.com/cn"
    page = webpage.WebPage(url).get_page()
    mainpage = webpage.MainPage(url)
    mainpage.set_login_page_tag_attrs(attrs=("li", {"id": "unav_sign-in"}))
    pageurl = mainpage.login_page_url(mainpage.get_page())


def display_cookie(cookie):
    for i, txt in enumerate(cookie):
        debug.debug('[%d],[%s]' % (i, txt))


def get_value(soup,idname, tagname='input', attrs=None):
    tmpattrs = None
    if attrs:
        tmpattrs = attrs
    else:
        tmpattrs = {'id': idname}
    try:
        result = soup.find(tagname, attrs=tmpattrs)
        return result.get('value')
    except AttributeError as e:
        debug.error('tagname %s %s' % (tagname, str(e)))


def build_post_data(soup, build_items):
    # Env
    post_data = {}
    for tag in build_items:
        post_data[tag] = get_value(soup, tag)

    return post_data


def get_geniusbar_page(store_number,
                   baseurl='http://concierge.apple.com/geniusbar/',
                   headers={}):
    page = webpage.WebPage(baseurl+store_number, None, headers=headers)
    data = page.get_data()
    Writefile('data/%s.html' % store_number, data.encode('utf-8'))
    return (data ,page)


def test_login_page():
    baseUrl = "http://www.apple.com"
    storelist = "http://www.apple.com/cn/retail/storelist/"
    mainpage = webpage.WebPage(storelist)
    data = mainpage.get_data()
    headers = {}
    headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
    headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    headers["Connection"] = 'keep-alive'
    headers["Accept-Encoding"] = "gzip, deflate"
    #print(headers)

    #f = open('data/storelist.html', 'w')
    #f.write(data.encode('utf-8'))
    Writefile('data/storelist.html', data.encode('utf-8'))
    data = data.encode('utf-8')
    soup = mainpage.get_page(data)
    # find all store
    #<div id="cnstores" class="listing">
    attrs = {"id":"cnstores","class":"listing"}
    tag = soup.find('div', attrs=attrs)
    hrefs = tag.findAll('a')
    suburl = None
    storeName = None
    for href in hrefs:
        suburl = href.get('href')
        storeName = href.getString().encode('utf-8', 'ignore')
        break

    storeurl = baseUrl + suburl
    debug.debug('%s: %s' % (storeName, storeurl))
    storepage = webpage.WebPage(storeurl)
    page_soup = storepage.get_page()
    Writefile('data/%s.html' % storeName.encode('gbk'), data)

    attrs = {'class': "nav hero-nav selfclear"}
    navtag = page_soup.find('nav', attrs=attrs)
    hrefs = navtag.findAll('a')
    support_url = None
    for href in hrefs:
        target = href.find('img', {'alt':'Genius Bar'})
        if target:
            support_url = href.get('href')
            break
    post_data = {}
    support_page = webpage.WebPage(support_url)
    data = support_page.get_data()
    Writefile('data/support_page.html', data.encode('utf-8'))
    page_soup = support_page.get_page(data)
    # get form token
    attrs = {'type': 'hidden', "name": "_formToken"}
    tokentag = page_soup.find('input', attrs=attrs)
    post_data["_formToken"] = tokentag.get('value')
    # get selected store
    attrs = {'selected': 'selected'}

    store_tag = page_soup.find('option', attrs=attrs)
    post_data['storeNumber'] = store_tag.get('value')
    post_data['store'] = post_data['storeNumber']
    store_number = post_data['store']
    post_data['ruleType'] = 'TECHSUPPORT'
    headers['Referer'] = support_url
    headers['Host'] = 'concierge.apple.com'
    #headers['POST'] = '/reservation/ HTTP/1.1'
    url = "http://concierge.apple.com/reservation/"
    jump_page = webpage.WebPage(url, urllib.urlencode(post_data))#, headers=headers)
    data = jump_page.get_data()
    Writefile('data/jump_page.html', data.encode('utf-8'))
    base_geniusbar = 'http://concierge.apple.com/geniusbar/'
    geniusbar_url = 'http://concierge.apple.com/geniusbar/' + post_data['store']
    headers = {}
    headers['Accept-Language']='zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
    headers['User-Agent']="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
    headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    headers["Connection"] = 'keep-alive'
    headers['Referer'] = support_url
    headers['Host'] = 'concierge.apple.com'
    geniusbar_page = webpage.WebPage(geniusbar_url,None, headers=headers)
    data = geniusbar_page.get_data()
    Writefile('data/getr401.html', data.encode('utf-8'))
    # post geniusbar store
    headers['Referer'] = geniusbar_url
    geniusbar_soup = geniusbar_page.get_page(data)
    attrs = {'type': 'hidden', "name": "_formToken"}
    tokentag = geniusbar_soup.find('input', attrs=attrs)
    post_data = {}
    post_data["_formToken"] = tokentag.get('value')
    post_data['supportOffered'] = 'true'
    geniusbar_detail_page = webpage.WebPage(geniusbar_url,
                                            urllib.urlencode(post_data),
                                            headers=headers)
    data = geniusbar_detail_page.get_data()
    Writefile('data/geniusbar_%s.html' % store_number, data)

    authenticate_url = 'https://idmsa.apple.com/IDMSWebAuth/authenticate'
    tag_names = ['Env', 'appIdKey', 'captchaType', 'captchaToken',
                 'grpCode', 'language', 'iForgotNewWindowVar',
                 'paramcode', 'path', 'path2', 'segment']

    post_data = build_post_data(geniusbar_detail_page.get_page(data), tag_names)
    post_data['accountPassword'] = 'Qq654123'
    post_data['appleId'] = 'zhonghui944oe@163.com'

    authenticate_page = webpage.WebPage(authenticate_url,
                                        data=urllib.urlencode(post_data),
                                        headers=headers)

    data = authenticate_page.get_data()
    Writefile('data/authenticate_page.html',data.encode('utf-8'))

    # post government id
    geniusbar_url ="https://concierge.apple.com/geniusbar/%s/governmentID" % store_number
    post_items =[
        'clientTimezone', 'FirstName', 'LastName'
        ]
    page_soup = authenticate_page.get_page(data)
    post_data = build_post_data(page_soup, post_items)
    if not post_data['clientTimezone']:
        post_data['clientTimezone'] = 'Asia/Shanghai'
    attrs = {'type': 'hidden', "name": "_formToken"}
    tokentag = page_soup.find('input', attrs=attrs)
    post_data["_formToken"] = tokentag.get('value')
    post_data['governmentID'] = '610102196103120670'
    post_data['governmentIDType'] = 'CN.PRCID'
    post_geniusbar_governmentid = webpage.WebPage(geniusbar_url,
                                                  urllib.urlencode(post_data),
                                                  headers)
    data = post_geniusbar_governmentid.get_data()
    page_soup = post_geniusbar_governmentid.get_page(data)
    Writefile('data/post_government_id.html', data.encode('utf-8'))
    data, geniusbar_page = get_geniusbar_page(store_number, headers=headers)
    page_soup = geniusbar_page.get_page(data)

    post_items = ['clientTimezone']
    post_data = build_post_data(page_soup, post_items)
    if not post_data['clientTimezone']:
        post_data['clientTimezone'] = 'Asia/Shanghai'
    attrs = {'type': 'hidden', "name": "_formToken"}
    tokentag = page_soup.find('input', attrs=attrs)
    post_data["_formToken"] = tokentag.get('value')
    attrs = {'class': 'NSCSSStateHidden value', "name": "id"}
    spantag = page_soup.find('span', attrs=attrs)
    post_data['id'] = spantag.text
    postbar = 'http://concierge.apple.com/geniusbar/R401'
    headers['Referer'] = postbar
    headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
    reservicepage = webpage.WebPage(postbar,
                                    data=urllib.urlencode(post_data),
                                    headers=headers)
    data = reservicepage.get_data()
    Writefile('data/revers.html', data.encode('utf-8'))
    page_soup = reservicepage.get_page(data)
    attrs = {'id':'captchaKey'}
    tag_key = page_soup.find("input", attrs=attrs)
    get_data ={}
    get_data['key'] = tag_key.get('value')
    attrs= {'id':"captchaFormat"}
    tag_format = page_soup.find("input", attrs=attrs)
    get_data['format'] = tag_format.get('value')
    import time
    get_data['t'] = str(time.time()).replace('.', '')
    url = "https://concierge.apple.com/geniusbar/R401/captcha?&%s" % urllib.urlencode(get_data)
    headers['Accept'] = 'image/png,image/*;q=0.8,*/*;q=0.5'
    headers['Accept-Encoding']='gzip, deflate'
    request = urllib2.Request(url, headers=headers)
    res = urllib2.urlopen(request)
    data = res.read()
    f= open('data/img.jpg', 'wb')
    f.write(data)
    f.close
test_login_page()

