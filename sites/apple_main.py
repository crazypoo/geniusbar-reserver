import sys
sys.path.append('../')
import urllib
from apple_genius_bar.store_page import GeniusbarPage
from utils import debug, Writefile


class AppleGeniusBarReservation(object):
    stores = None
    host = 'http://www.apple.com'
    def __init__(self):

        self.appleid = None
        self.passwd = None
        self.governmentId = None
        self.reservationUrl = "http://concierge.apple.com/reservation/"
        self.authUrl = "https://idmsa.apple.com/IDMSWebAuth/authenticate"
        self.govUrlFormat = "https://concierge.apple.com/geniusbar/%s/governmentID"
        self.supportUrl = None
        self.verifyData = None
        self.status = None
        self.progress = 0
        GeniusbarPage._init_headers()

    @classmethod
    def Init_stores_list(self):
        storeListurl = 'http://www.apple.com/cn/retail/storelist/'
        page = GeniusbarPage(storeListurl)
        AppleGeniusBarReservation.stores = page.get_store_list()
        return AppleGeniusBarReservation.stores

    @classmethod
    def Get_store_url(self, suburl):
        return AppleGeniusBarReservation.host + suburl

    @classmethod
    def Get_suppport_url(self, storeUrl):
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
        return page

    def get_geniusbar_page(self, prePage):
        debug.debug('GET %s' % GeniusbarPage.get_geniusbar_url())
        headers = GeniusbarPage.headers
        headers['Referer'] = prePage.get_url()
        headers["Host"] = 'concierge.apple.com'
        geniusbarPage = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                      headers=headers)
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
        return authPage

    def get_techsupport_page(self, url):
        debug.debug('GET %s' % url)
        page = GeniusbarPage(url)
        return page

    def jump_login_page(self, supporturl, result=None):
        self.progress = 10
        supportPage = self.get_techsupport_page(supporturl)
        self.progress = 20
        # get selected store
        self.post_reserv_page(supportPage)
        # ###
        self.progress = 30
        getGeniusbarPage = self.get_geniusbar_page(supportPage)
        self.progress = 40

        postGeniusPage = self.post_geniusbar_page(getGeniusbarPage)
        self.progress = 50
        # # auth
        authPage = self.post_anth_page(postGeniusPage)
        self.progress = 60

        # ## send governmentId
        governmentUrl = self.govUrlFormat % GeniusbarPage.storeNumber
        govPage = self.post_governmenid(governmentUrl, authPage)
        self.progress = 70

        smschallengePage = self.post_smschallenge(govPage)
        Writefile('tmp/smschallengepage.html', smschallengePage.get_data())
        self.progress = 80
        # validity check<div autocomplete="off" id="SmsCode.ID142" type="text" name="SmsCode" class="ValidatedField SmsCode"
        if not smschallengePage.check('div', {'class': "ValidatedField SmsCode"}):
            # get validcode picture
            self.verifyData = smschallengePage.get_verification_code_pic()
            # f = open('data/verifyCode.jpg', 'wb')
            # f.write(self.verifyData)
            # f.close()
            self.progress = 90
            if self.verifyData:
                debug.info('Successful')
                self.status = True
                if result:
                    result.put(self.verifyData)
            else:
                self.status = False
                debug.error('verfyData error')
            self.progress = 100
            return self.verifyData
        else:
            debug.error('not finished')
            self.progress = 100
            return None

    def post_governmenid(self, url, prepage):
        debug.debug('post %s' % url)
        postData = prepage.build_governmentid_post_data()
        postData["_formToken"] = prepage.get_formtoken_value()
        postData['governmentID'] = GeniusbarPage.governmentId
        postData['governmentIDType'] = 'CN.PRCID'
        if not postData['clientTimezone']:
            postData['clientTimezone'] = 'Asia/Shanghai'
        headers = GeniusbarPage.headers
        headers['Referer'] = prepage.get_url()
        gnPage = GeniusbarPage(url,
                               urllib.urlencode(postData),
                               headers)
        return gnPage

    def post_smschallenge(self, prePage):
        '''
        "serviceType_iPhone"
        "serviceType_iPad"
        "serviceType_iPod"
        "serviceType_Mac"
        '''
        debug.debug('post %s' % GeniusbarPage.get_geniusbar_url())
        postData = prePage.build_smschallenge_post_data("serviceType_Mac")
        headers = GeniusbarPage.headers
        headers['Referer'] = GeniusbarPage.get_geniusbar_url()
        smschallenge = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                     urllib.urlencode(postData),
                                     headers=GeniusbarPage.headers)
        return smschallenge

    def isCompleted(self, result=None):
        if result:
            result.put((self.status, self.progress))
            return self.status
        return self.status
