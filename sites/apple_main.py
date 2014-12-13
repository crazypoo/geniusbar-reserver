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
        # http://concierge.apple.com/geniusbar/R448/reservationConfirmation
        self.reservConfirmFormat = 'http://concierge.apple.com/geniusbar/%s/reservationConfirmation'
        self.challengeUrlFormat = 'https://concierge.apple.com/geniusbar/%s/smschallenge'
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
        debug.debug('get storeurl')
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

    @classmethod
    def Get_workshops_url(self, storeUrl):
        page = GeniusbarPage(storeUrl)
        data = page.get_data()
        Writefile('debug/workshops.html', data)
        attrs = {'class': "nav hero-nav selfclear"}
        page_soup = page.get_soup()
        navtag = page_soup.find('nav', attrs=attrs)
        hrefs = navtag.findAll('a')
        url = None
        for href in hrefs:
            target = href.find('img', {'alt': 'Workshops'})
            if target:
                url = href.get('href')
                break
        return url

    def post_reserv_page(self, prePage, rultype='TECHSUPPORT'):
        postData = {}
        postData['_formToken'] = prePage.get_formtoken_value()
        attrs = {'selected': 'selected'}
        postData['storeNumber'] = prePage.get_tag_value('option', attrs=attrs)
        GeniusbarPage.storeNumber = postData['storeNumber']
        postData['store'] = GeniusbarPage.storeNumber
        postData['ruleType'] = rultype
        page = GeniusbarPage(self.reservationUrl,
                             urllib.urlencode(postData))
        return page

    def get_geniusbar_page(self, prePage):
        headers = GeniusbarPage.headers
        headers['Referer'] = prePage.get_url()
        headers["Host"] = 'concierge.apple.com'
        geniusbarPage = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                      headers=headers)
        return geniusbarPage

    def post_geniusbar_page(self, prePage):

        postData = {}
        postData["_formToken"] = prePage.get_formtoken_value()
        postData['supportOffered'] = 'true'
        headers = GeniusbarPage.headers
        headers['Referer'] = prePage.get_url()
        geniusbarPage = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                      data=urllib.urlencode(postData),
                                      headers=headers)
        return geniusbarPage

    def post_anth_page(self, prePage):

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

    def buildPostTimeSlotsData(self, page):
        '''
        '''
        postData = {}
        postData['_formToken'] = page.get_formtoken_value()
        return postData

    def buildTimeSlotsTable(self, page):
        '''
        '''
        # json data [{'week':[(time, key), ...]]
        # for test
        soup = page.get_soup()
        attrs = {'id': 'dayC'}
        daycs = soup.findAll('div', attrs=attrs)
        maxRow = 0
        ret = []
        for dayc in daycs:
            item = {}
            times = []
            dayName = dayc.find('a', {'id': 'dayNameC'}).text.replace(' ', '')
            slot_inners = dayc.findAll('div', {'class': 'slot_inner'})
            for slot_inner in slot_inners:
                timeslots = slot_inner.findAll('a', {'id': 'timeslotC'})
                for timeslot in timeslots:
                    if not timeslot.contents:
                        print('tiemslot have no contents')
                        continue
                    timetag = timeslot.find('span', {'id': 'timeslotNameC'})
                    time = timetag.text
                    idtag = timeslot.find('span', {'name': 'id'})
                    id = idtag.text
                    times.append((time, id))
                item[dayName] = times
                size = len(times)
                if size > maxRow:
                    maxRow = size
            ret.append(item)
        return (ret, maxRow)

    def afterReserWorkShops(self, page, taskStatus):
        runningtime = 300
        while runningtime > 0:
            taskCmd = taskStatus['taskCmd']
            if taskCmd == 'timeslot':
                data, rowmax = self.buildTimeSlotsTable(page)
                taskStatus['timeSlots'] = (data, rowmax)
                taskStatus['taskCmd'] = None
                taskStatus['cmdStatus'] = 'OK'
                break
            runningtime -= 1
            time.sleep(1)
            print('waitingCmd')

    def waitingCmd(self, page, taskStatus):
        '''
        waiting the input
        '''
        runtime = 300  # waiting time
        storeUrl = taskStatus['storeUrl']
        debug.debug(storeUrl)

        while runtime > 0:
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
                postData['clientTimezone'] = taskStatus['clientTimezone']
                # 'Asia/Shanghai'
                submitUrl = self.challengeUrlFormat % GeniusbarPage.storeNumber
                headers = page.headers
                headers['Referer'] = submitUrl
                headers.pop('Accept-Encoding')
                submitpage = GeniusbarPage(submitUrl,
                                           data=urllib.urlencode(postData),
                                           headers=headers)
                data = submitpage.get_data()
                resultfile = 'tmp/%s.htm' % taskStatus['appleId']
                Writefile(resultfile, data)

                attrs = {"class": "error-message on",
                         "id": "error_message_generalError"}
                errorMsg = submitpage.get_tag_text('label', attrs=attrs)
                if errorMsg:
                    taskStatus['cmdStatus'] = 'NOK'
                    taskStatus['taskCmd'] = None
                    taskStatus['prompInfo'] = errorMsg
                    page = submitpage
                    debug.error(errorMsg)
                    Writefile('tmp/submiterr.html', page.get_data())
                    continue
                else:
                    # success for submit
                    # get the time slots
                    ret, maxrow = self.buildTimeSlotsTable(submitpage)
                    taskStatus['cmdStatus'] = 'OK'
                    taskStatus['timeSlots'] = (ret, maxrow)
                    taskStatus['taskCmd'] = None
                    page = submitpage
                    continue
            if taskCmd == 'timeslot':
                # post timeslots
                debug.debug('get timeslot cmd %s' % taskStatus['appleId'])
                postData = self.buildPostTimeSlotsData(page)
                postData['clientTimezone'] = taskStatus['clientTimezone']
                postData['id'] = taskStatus['id']
                tlsUrl = self.timeslotFormat % GeniusbarPage.storeNumber
                debug.debug('tls ulr %s' % tlsUrl)
                headers = {}
                headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
                headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
                headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                headers["Connection"] = 'keep-alive'
                headers["Host"] = 'concierge.apple.com'
                tlspage = GeniusbarPage(tlsUrl,
                                        data=urllib.urlencode(postData),
                                        headers=headers)
                data = tlspage.get_data()
                Writefile('tmp/posttimeslotsresult.html', data)
                text = self.getConfirmMsg(tlspage)
                taskStatus['prompInfo'] = text.replace(' ', '')
                Writefile('tmp/reserv-%s' % taskStatus['appleId'],
                          taskStatus['prompInfo'])
                taskStatus['taskCmd'] = None
                taskStatus['cmdStatus'] = 'OK'
                break
            if taskCmd == 'end':
                taskStatus['taskCmd'] = None
                break
            #debug.debug('waiting cmd')
            time.sleep(1)
            runtime -= 1
        debug.info('End task %s' % taskStatus['appleId'])

    def getConfirmMsg(self, page):
        soup = page.get_soup()
        divtag = soup.find('div', attrs={'class': 'col-first'})
        ul = divtag.find('ul')
        return ul.text

    def Jump_workshops_page(self, enterUrl, taskStatus=None):
        self.initUrls()
        self.taskStatus = taskStatus
        print('workshops %s' % enterUrl)
        wkshpg = GeniusbarPage(enterUrl)
        print(wkshpg)
        #self.update_progress(20)
        #Writefile('debug/wkspage.html', wkshpg.get_data())
        self.update_progress(30)
        reserpage = self.post_reserv_page(wkshpg, 'WORKSHOP')
        #Writefile('debug/geniuspage.html', reserpage.get_data())
        workshopsurl = 'http://concierge.apple.com/workshops/' + GeniusbarPage.storeNumber
        self.update_progress(60)

        #genpage = self.get_geniusbar_page(wkshpg)
        postData = {}
        postData['id'] = '5756055972603593735'
        postData['_formToken'] = reserpage.get_formtoken_value()
        postData['workshopTypeName'] = 'CUSTOM_WORKSHOP'
        timeslotpage = GeniusbarPage(workshopsurl,
                                     data=urllib.urlencode(postData),
                                     headers=GeniusbarPage.headers)
        self.update_progress(100)
        self.afterReserWorkShops(timeslotpage, taskStatus)
       # Writefile('debug/timeslots.html', timeslotpage.get_data())

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
        reservType = self.loginData['reservType']
        postData = prePage.build_smschallenge_post_data(reservType)
        headers = GeniusbarPage.headers
        headers['Referer'] = GeniusbarPage.get_geniusbar_url()
        smschallenge = GeniusbarPage(GeniusbarPage.get_geniusbar_url(),
                                     urllib.urlencode(postData),
                                     headers=GeniusbarPage.headers)
        return smschallenge
