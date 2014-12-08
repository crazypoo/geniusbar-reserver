# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import urllib
from apple_genius_bar.store_page import GeniusbarPage
from utils import debug, Writefile
import time


class AppleGeniusBarReservation(object):
    stores = None
    host = 'http://www.apple.com'

    def __init__(self, loginData):

        self.reservationUrl = "http://concierge.apple.com/reservation/"
        self.authUrl = "https://idmsa.apple.com/IDMSWebAuth/authenticate"

        self.loginData = loginData
        GeniusbarPage._init_headers()

    def initUrls(self):
        self.reservationUrl = "http://concierge.apple.com/reservation/"
        self.authUrl = "https://idmsa.apple.com/IDMSWebAuth/authenticate"
        self.govUrlFormat = "https://concierge.apple.com/geniusbar/%s/governmentID"
        self.timeslotFormat = "http://concierge.apple.com/geniusbar/%s/timeslots"
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
        # 'Qq654123'
        postData['accountPassword'] = self.loginData['accountPassword']
        postData['appleId'] = self.loginData['appleId']
        # 'zhonghui944oe@163.com'
        headers = GeniusbarPage.headers
        headers['Host'] = "concierge.apple.com"
        headers['Referer'] = prePage.get_url()
        authPage = GeniusbarPage(self.authUrl,
                                 data=urllib.urlencode(postData),
                                 headers=headers)
        return authPage

    def get_techsupport_page(self, url):
        # debug.debug('GET %s' % url)
        headers = GeniusbarPage.headers
        # print('heaader %s' % headers)
        page = GeniusbarPage(url, headers=headers)
        return page

    def update_progress(self, progress):
        if self.taskStatus:
            self.taskStatus['taskProgress'] = progress

    def debugstep(self):
        self.update_progress(100)

    def waitingCmd(self, page, taskStatus):
        '''
        waiting the input
        '''
        debug.debug('Enter waiting cmd')
        runtime = 300  # waiting time
        storeUrl = taskStatus['storeUrl']
        debug.debug(storeUrl)
        while True and runtime > 0:
            taskCmd = taskStatus['taskCmd']
            if taskCmd == 'refresh':
                debug.debug('refresh cmd %s' % taskStatus['appleId'])
                verifycodedata, tSt = page.get_verification_code_pic()
                taskStatus['verifyCodeData'] = verifycodedata
                taskStatus['taskCmd'] = None
                time.sleep(1)
                continue
            if taskCmd == 'submit':
                debug.debug('get submit cmd %s' % taskStatus['appleId'])
                postData = page.build_submit_post_data()
                postData['captchaAnswer'] = taskStatus['captchaAnswer']
                postData['phoneNumber'] = taskStatus['phoneNumber']
                postData['smsCode'] = taskStatus['smsCode']
                # 'Asia/Shanghai'
                submitUrl = GeniusbarPage.challengeUrlFormat % GeniusbarPage.storeNumber
                headers = page.headers
                headers['Referer'] = submitUrl
                headers.pop('Accept-Encoding')
                print(headers)
                submitpage = GeniusbarPage(submitUrl,
                                           data=urllib.urlencode(postData),
                                           headers=headers)
                data = submitpage.get_data()
                resultfile = 'tmp/%s.htm' % taskStatus['appleId']
                Writefile(resultfile, data)
                tlsUrl = self.timeslotFormat % GeniusbarPage.storeNumber
                tlspage = GeniusbarPage(tlsUrl, headers=headers)
                data = tlspage.get_data()
                Writefile('last.html', data)
                taskStatus['taskCmd'] = None
                # gzip, deflate
                # http://www.apple.com/cn/retail/shanghaiiapm/
                break
            if taskCmd == 'end':
                taskStatus['taskCmd'] = None
                break
            #debug.debug('waiting cmd')
            time.sleep(1)
            runtime -= 1
        debug.info('End task %s' % taskStatus['appleId'])

    def Jump_login_page(self, supporturl, taskStatus=None):
        self.initUrls()
        self.taskStatus = taskStatus
        self.update_progress(10)
        supportPage = self.get_techsupport_page(supporturl)
        self.update_progress(20)
        # get selected store
        self.post_reserv_page(supportPage)
        # ###
        self.update_progress(30)
        getGeniusbarPage = self.get_geniusbar_page(supportPage)
        self.update_progress(40)

        postGeniusPage = self.post_geniusbar_page(getGeniusbarPage)
        self.update_progress(50)
        # # auth
        authPage = self.post_anth_page(postGeniusPage)
        self.update_progress(60)

        # ## send governmentId
        governmentUrl = self.govUrlFormat % GeniusbarPage.storeNumber
        govPage = self.post_governmenid(governmentUrl, authPage)
        self.update_progress(70)
        smschallengePage = self.post_smschallenge(govPage)
        # Writefile('tmp/smschallengepage.html', smschallengePage.get_data())
        self.update_progress(80)
        text = smschallengePage.get_smschalleng_steps()
        if not text:
            msg = 'Reserved failed %s' % self.taskStatus['appleId']
            debug.error(msg)
            self.taskStatus['prompInfo'] = msg
            self.update_progress(100)
            # self.waitingCmd(smschallengePage, taskStatus)
            return None
        self.taskStatus['prompInfo'] = text
        self.update_progress(85)
        attrs = {'class': "ValidatedField SmsCode"}
        if not smschallengePage.check('div', attrs):
            # get validcode picture
            self.update_progress(86)
            verifyData, tSt = smschallengePage.get_verification_code_pic()
            self.update_progress(87)
            if verifyData:
                self.taskStatus['verifyCodeData'] = verifyData
                # WriteVerifyPic('tmp/%s.jpg' % tSt, verifyData)
                self.update_progress(100)
                self.waitingCmd(smschallengePage, taskStatus)
                # get the smschallenge info phone number
            else:
                debug.error('verfyData error')
            self.update_progress(100)
            return verifyData

        self.update_progress(100)
        return None

    def post_governmenid(self, url, prepage):
        debug.debug('post %s' % url)
        postData = prepage.build_governmentid_post_data()
        postData["_formToken"] = prepage.get_formtoken_value()
        postData['governmentID'] = self.loginData['governmentID']
        postData['governmentIDType'] = self.loginData['governmentIDType']
        #'CN.PRCID'
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
        reservType = self.loginData['reservType']
        postData = prePage.build_smschallenge_post_data(reservType)
        headers = GeniusbarPage.headers
        headers['Referer'] = GeniusbarPage.get_geniusbar_url()
        smschallenge = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                     urllib.urlencode(postData),
                                     headers=GeniusbarPage.headers)
        return smschallenge
