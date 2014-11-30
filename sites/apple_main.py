import sys
sys.path.append('../')
import urllib
from apple_genius_bar.store_page import GeniusbarPage
from utils import debug, Writefile


class AppleGeniusBarReservation(object):
    def __init__(self):
        self.stores = {}
        self.host = 'http://www.apple.com'
        self.appleid = None
        self.passwd = None
        self.governmentId = None
        self.reservationUrl = "http://concierge.apple.com/reservation/"
        self.authUrl = "https://idmsa.apple.com/IDMSWebAuth/authenticate"
        self.supportUrl = None
        GeniusbarPage._init_headers()

    def init_stores_list(self):
        storeListurl = 'http://www.apple.com/cn/retail/storelist/'
        page = GeniusbarPage(storeListurl)
        self.stores = page.get_store_list()
        return self

    def get_store_list(self):
        return self.stores

    def get_store_url(self, suburl):
        return self.host + suburl


    def get_suppport_url(self, storeUrl):
        page = GeniusbarPage(storeUrl)
        attrs = {'class': "nav hero-nav selfclear"}
        page_soup = page.get_soup()
        navtag = page_soup.find('nav', attrs=attrs)
        hrefs = navtag.findAll('a')
        support_url = None
        for href in hrefs:
            target = href.find('img', {'alt': 'Genius Bar'})
            if target:
                support_url = href.get('href')
                break
        return support_url
    
    def post_reserv_page(self, prePage):
        debug.debug('post %s' % self.reservationUrl)
        postData = {}
        postData['_formToken'] = prePage.get_formtoken_value()
        attrs = {'selected': 'selected'}
        postData['storeNumber'] = prePage.get_tag_value('option', attrs=attrs)
        GeniusbarPage.storeNumber = postData['storeNumber']
        postData['store'] = GeniusbarPage.storeNumber
        postData['ruleType'] = 'TECHSUPPORT'
        page = GeniusbarPage(self.reservationUrl,
                             urllib.urlencode(postData))
        Writefile('data/post_reserv_page.html', page.get_data())
        return page

    def get_geniusbar_page(self, prePage):
        debug.debug('GET %s' % GeniusbarPage.get_geniusbar_url())
        headers = GeniusbarPage.headers
        headers['Referer'] = prePage.get_url()
        headers["Host"] = 'concierge.apple.com'
        geniusbarPage = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                      headers=headers)
        Writefile('data/get_geniusbar_page.html', geniusbarPage.get_data())
        return geniusbarPage

    def post_geniusbar_page(self, prePage):
        debug.debug('POST %s' % GeniusbarPage.get_geniusbar_url())
        postData = {}
        postData["_formToken"] = prePage.get_formtoken_value()
        postData['supportOffered'] = 'true'
        headers = GeniusbarPage.headers
        headers['Referer'] = prePage.get_url()
        headers["Host"] = 'concierge.apple.com'
        geniusbarPage = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                      data=urllib.urlencode(postData),
                                      headers=headers)
        Writefile('data/geniusbarPage.html', geniusbarPage.get_data())
        return geniusbarPage

    def post_anth_page(self, prePage):
        debug.debug('POST %s' % self.authUrl)
        postData = prePage.build_auth_post_data()
        GeniusbarPage.set_user_data(appleId='zhonghui944oe@163.com',
                                    passwd='Qq654123',
                                    governmentId='610102196103120670')
        postData['accountPassword'] = 'Qq654123'
        postData['appleId'] = 'zhonghui944oe@163.com'
        headers = GeniusbarPage.headers
        headers['Host'] = "concierge.apple.com"
        headers['Referer'] = prePage.get_url()
        authPage = GeniusbarPage(self.authUrl,
                                 data=urllib.urlencode(postData),
                                 headers=headers)
        Writefile('data/authPage.html', authPage.get_data())
        return authPage

    def get_techsupport_page(self, url):
        debug.debug('GET %s' % url)
        page = GeniusbarPage(url)
        Writefile('data/support_page.htm', page.get_data())
        return page

    def jump_login_page(self, supporturl):
        supportPage = self.get_techsupport_page(supporturl)

        # get selected store
        reservPage = self.post_reserv_page(supportPage)
        # ###
        getGeniusbarPage = self.get_geniusbar_page(supportPage)
        postGeniusPage = self.post_geniusbar_page(getGeniusbarPage)
        # # auth
        authPage = self.post_anth_page(postGeniusPage)
        # ## send governmentId
        governmentUrl = "https://concierge.apple.com/geniusbar/%s/governmentID" % GeniusbarPage.storeNumber
        govpage = self.post_governmenid(governmentUrl, authPage)
        getGeniusbarPage = self.get_geniusbar_page(postGeniusPage)
        self.post_smschallenge(getGeniusbarPage)

    def post_governmenid(self, url, prepage):
        debug.debug('post %s' % url)
        postData = prepage.build_governmentid_post_data()
        postData["_formToken"] = prepage.get_formtoken_value()
        postData['governmentID'] = GeniusbarPage.governmentId
        print(postData['governmentID'])
        postData['governmentIDType'] = 'CN.PRCID'
        if not postData['clientTimezone']:
            postData['clientTimezone'] = 'Asia/Shanghai'
        headers = GeniusbarPage.headers
        headers['Referer'] = prepage.get_url()
        gnPage = GeniusbarPage(url,
                               urllib.urlencode(postData),
                               headers)
        Writefile('data/aftergovernmentid.html', gnPage.get_data())
        return gnPage

    def post_smschallenge(self, prePage):
        '''
        "serviceType_iPhone"
        "serviceType_iPad"
        "serviceType_iPod"
        "serviceType_Mac"
        '''
        debug.debug('post %s' % GeniusbarPage.get_geniusbar_url())
        postData = prePage.build_smschallenge_post_data("serviceType_iPhone")
        headers = GeniusbarPage.headers
        headers['Referer'] = GeniusbarPage.get_geniusbar_url()
        smschallenge = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                     urllib.urlencode(postData),
                                     headers=GeniusbarPage.headers)
        Writefile('data/smschallenge.html',smschallenge.get_data())
        return smschallenge
