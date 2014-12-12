# -*- coding: utf-8 -*-
import os
import PyQt4.QtGui as QtGui
from PyQt4.QtGui import QSplitter, QLabel
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import QSize
from utils import debug  # , WriteVerifyPic
from uidesigner.ui_mainwindow_splitter import Ui_MainWindow
from uidesigner import taskviewwidget
from sites.apple_main import AppleGeniusBarReservation
from taskmanagedlg import TaskManageDLG
from tasklistdlg import TaskListDLG
from accountmanagedlg import AccountManagerDLG
from accountlistdlg import AccountListDLG
from sites.apple_genius_bar.confhelper import AccountManager
import multiprocessing
from multiprocessing import Manager, Pool
import threading
import time
import cookielib
from tablewidget import TableWidget


class ApplyTask(object):
    def __init__(self, loginData):
        self.loginData = loginData
        self.reser = AppleGeniusBarReservation(loginData)
        self.enterUrl = loginData['enterUrl']

    def applyGeniusbar(self, taskStatus):
        debug.debug('start %s' % taskStatus['appleId'])
        return self.reser.Jump_login_page(self.enterUrl,
                                          taskStatus)

    def applyWorkshops(self, taskStatus):
        return self.reser.Jump_workshops_page(self.enterUrl,
                                              taskStatus)


def Reserver(applyTask, taskStatus, geniusbar=True):
    name = multiprocessing.current_process().name
    debug.debug(name)
    if geniusbar:
        return applyTask.applyGeniusbar(taskStatus)
    else:
        return applyTask.applyWorkshops(taskStatus)


class ReserverResult:
    """
    save the reserv result
    """
    def __init__(self):
        self.result = {}

    def add(self, taskName, result):
        '''
        {taskname:[{applid,xx},{}]}
        '''
        if taskName not in self.result.keys():
            self.result[taskName] = []
        self.result[taskName].append(result)

    def _getTaskResult(self, taskName):
        if taskName in self.result.keys():
            return self.result[taskName]

    def update(self, taskName, appleid, key, value):
        result = self._getTaskResult(taskName)
        for r in result:
            if appleid in r.values():
                r[key] = value

    def getData(self, taskName):
        return self._getTaskResult(taskName)


class AppContext():
    def __init__(self, cwd, mainWindow):
        self.configurefileDir = cwd
        self.accountManagerDLG = None
        self.taskManageDLG = None
        self.tasklistDLG = None
        self.proxyManagerDLG = None
        self.accountManager = None
        self.currentTaskList = None
        self.accountListDLG = None
        self.mainWindow = mainWindow

    def getDefaultTaskFile(self):
        return os.path.join(self.configurefileDir,
                            'res/task',
                            'defaulttask.tkl')

    def getAccountFile(self):
        return os.path.join(self.configurefileDir,
                            'res/accounts',
                            'account.dat')

    def getTaskStoreDir(self):
        return os.path.join(self.configurefileDir, 'res', 'task')

    def getCurrentTask(self):
        return self.currentTaskList

    def __getattr__(self, name):
        return getattr(self.mainWindow, name)

    def setCurrentTask(self, task):
        self.currentTaskList = task
        self.msgLabel.setText('Current Task is: %s' % task.taskName)

    def getCurrentTaskName(self):
        if self.currentTaskList:
            return self.currentTaskList.taskName


class MainWindow(QtGui.QMainWindow):
    signalViewTask = pyqtSignal(int)
    signalUpdateProgress = pyqtSignal(str, str)
    signalStoreResult = pyqtSignal(str)
    # sigUpdateCurrentId = pyqtSignal()
    sigUpdateProgressBar = pyqtSignal(str)

    def setupTaskTable(self):

        headers = [
            u"账号",
            u"进度",
            u"代理",
            u"零售店",
            u"服务类型"
        ]
        self.taskTableWidget = TableWidget(headers=headers)

    def setupViews(self):
        splitter = QSplitter()
        self.setupTaskTable()
        splitter.addWidget(self.taskTableWidget)
        self.taskViewWidget = taskviewwidget.TaskViewWidget()
        splitter.addWidget(self.taskViewWidget)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        self.setCentralWidget(splitter)
        self.taskViewWidget.hide()

        self.msgLabel = QLabel()
        self.statusBar().addWidget(self.msgLabel)

    def __init__(self, abscwd, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupViews()
        self.appContext = AppContext(abscwd, self)
        self.setupMembers()
        self.setupSig2Slot()

    def setupMembers(self):
        self.reserverResult = ReserverResult()
        self.preSelectedRow = None
        self.store_suburl = {}
        self.storelist = []
        self.finishedAppleId = []
        self.initStoreData()
        self.running = False
        # ###################################
        accountfile = self.appContext.getAccountFile()
        self.appContext.accountManager = AccountManager(accountfile)
        self.appContext.accountManagerDLG = AccountManagerDLG(self.appContext)
        self.appContext.accountListDLG = AccountListDLG(self.appContext)
        self.taskManageDLG = TaskManageDLG(self.appContext,
                                           self.storelist,
                                           self.reservTypes)

        self.appContext.taskManageDLG = self.taskManageDLG
        self.appContext.tasklistDLG = TaskListDLG(self.appContext)

        # the apply process
        self.applyTasks = []

        self.appleIdToProgresscell = {}  # = {id, item}
        task = self.taskManageDLG.getDefaultTask()
        if task:
            self.appContext.setCurrentTask(task)
            self.fillTaskView(task)

    def setupSig2Slot(self):
        self.signalUpdateProgress.connect(self.updateProgress)
        self.signalStoreResult.connect(self.storeResult)
        # self.sigUpdateCurrentId.connect(self.updateCurrentApplIdProgress)
        self.sigTimeSlot.connect(self.selectTimeSlot)
        self.pBSubmit.clicked.connect(self.submit)
        self.pBRefresh.clicked.connect(self.refresh)

        self.taskTableWidget.cellClicked.connect(self.twTasklistCellClicked)

    def initStoreData(self):
        # the store name of each url
        self.stores = AppleGeniusBarReservation.Init_stores_list()
        for index, item in self.stores.items():
            self.store_suburl[item[0]] = item[1]
            self.storelist.append(item[0])

        self.reservTypes = ["serviceType_iPhone",
                            "serviceType_iPad",
                            "serviceType_iPod",
                            "serviceType_Mac"]

    def fillTaskView(self, task):
        accounts = task.getAccounts()
        rowCount = len(accounts)
        if rowCount is not 0:
            self.preSelectedRow = 0

        # self.ui.gBListName.setTitle(unicode(task.taskName))
        self.taskTableWidget.setRowCount(rowCount)
        row = 0
        for count in accounts:
            item = QtGui.QTableWidgetItem()
            item.setText(count['appleid'])
            self.taskTableWidget.setItem(row, 0, item)

            item = QtGui.QTableWidgetItem()
            item.setText("0")
            self.taskTableWidget.setItem(row, 1, item)
            self.appleIdToProgresscell[count['appleid']] = item
            item = QtGui.QTableWidgetItem()
            item.setText(task.proxyServer)
            self.taskTableWidget.setItem(row, 2, item)

            item = QtGui.QTableWidgetItem()
            item.setText(unicode(task.storeName))
            self.taskTableWidget.setItem(row, 3, item)

            item = QtGui.QTableWidgetItem()
            item.setText(task.reservType)
            self.taskTableWidget.setItem(row, 4, item)
            row += 1

    def getTaskPool(self):
        poolSize = multiprocessing.cpu_count() * 2
        return Pool(processes=poolSize)

    def accountManage(self):
        self.appContext.accountManagerDLG.exec_()
        # TODO:

    def taskManage(self):
        self.taskManageDLG.exec_()
        # TODO:

    def getTaskTable(self):
        return self.taskTableWidget

    def getTaskView(self):
        return self.taskViewWidget

    def twTasklistCellClicked(self, row, col):
        self.getTaskView().show()
        if col == 0:
            item = self.getTaskTable().item(row, 0)
            appleId = item.text()
            progress = self.getTaskTable().item(row, 1)
            progress = progress.text()
            self.progressBar.setValue(int(progress))
            account = self.appContext.accountManager.getAccount(appleId)
            if account:
                self.lEPhoneNumber.setText(account['phonenumber'])
            if int(progress) == 100:
                self.fillResultView(appleId)
        self.preSelectedRow = row

    def getTasksInfo(self, geniusBar=True):
        taskName = self.appContext.getCurrentTaskName()
        task = self.appContext.taskManageDLG.tasks[str(taskName)]
        accounts = task.getAccounts()
        storeName = task.storeName
        reservType = task.reservType
        suburl = self.store_suburl[unicode(storeName)]
        storeUrl = AppleGeniusBarReservation.Get_store_url(suburl)
        url = None
        if geniusBar:
            url = AppleGeniusBarReservation.Get_suppport_url(storeUrl)
        else:
            url = AppleGeniusBarReservation.Get_workshops_url(storeUrl)

        loginDatas = []
        for account in accounts:
            loginData = {}
            loginData['appleId'] = account['appleid']
            loginData['accountPassword'] = account['passwd']
            loginData['phoneNumber'] = account['phonenumber']
            loginData['governmentID'] = account['governmentid']
            loginData['governmentIDType'] = 'CN.PRCID'
            loginData['reservType'] = reservType
            loginData['storeName'] = storeName
            loginData['enterUrl'] = url
            loginData['storeUrl'] = storeUrl
            loginDatas.append(loginData)

        return loginDatas

    def createOpener(self):
        import urllib2
        cookie = cookielib.CookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookie_support)
        return opener

    def startTask(self):
        self.twTasklistCellClicked(0, 0)
        self.running = True
        self.disableStart()
        geniusBar = True
        loginDatas = self.getTasksInfo(geniusBar=geniusBar)
        self.statusTasks = []
        self.finishedAppleId = []
        pool = self.getTaskPool()
        for loginData in loginDatas:
            apy = ApplyTask(loginData)
            self.applyTasks.append(apy)
            taskStatus = Manager().dict()
            taskStatus['prompInfo'] = ''
            taskStatus['verifyCodeData'] = ''
            taskStatus['appleId'] = loginData['appleId']
            taskStatus['taskProgress'] = '0'
            taskStatus['taskCmd'] = None
            taskStatus['cmdStatus'] = None
            taskStatus['storeUrl'] = loginData['storeUrl']
            taskStatus['timeSlots'] = None
            # timeslot id
            taskStatus['id'] = None
            self.statusTasks.append(taskStatus)

            taskResult = Manager().dict()
            taskResult['appleId'] = loginData['appleId']
            self.finishedAppleId.append(taskStatus)

            pool.apply_async(Reserver, (apy, taskStatus, geniusBar))

        pool.close()
        debug.debug('have %s task' % len(self.statusTasks))
        checking = threading.Thread(target=self.checking,
                                    args=(self.statusTasks,
                                          self.finishedAppleId))
        checking.start()

    def updateProgress(self, appleId, progress):
        item = self.appleIdToProgresscell[str(appleId)]
        item.setText(progress)
        self.updateCurrentApplIdProgress(appleId)

    def updateCurrentApplIdProgress(self, appleId):
        rowindex = self.getTaskTable().currentRow()
        if rowindex == -1:
            if self.preSelectedRow:
                rowindex = self.preSelectedRow
            else:
                rowindex = 0
        self.preSelectedRow = rowindex

        appleIdItem = self.getTaskTable().item(rowindex, 0)
        appleId = appleIdItem.text()
        progressItem = self.getTaskTable().item(rowindex, 1)
        progress = int(progressItem.text())
        # self.getProcessBar().setValue(progress)
        self.progressBar.setValue(progress)
        if progress == 100:
            self.fillResultView(appleId)
            time.sleep(1)

    def __getattr__(self, name):
        ret = getattr(self.taskTableWidget, name)
        if not ret:
            ret = getattr(self.taskViewWidget, name)
        return ret

    def fillResultView(self, appleId):
        currentTaskName = self.appContext.getCurrentTaskName()
        results = self.reserverResult.getData(currentTaskName)
        if not results:
            debug.info('Can not find %s' % currentTaskName)
            return
        findResult = None
        for result in results:
            if appleId in result.values():
                findResult = result
        if not findResult:
            debug.error('can not found verifyData %s,%s'
                        % (appleId, currentTaskName))
            return
        verifyData = findResult['verifyCodeData']
        if verifyData:
            self.fillVerifyCodePic(verifyData)
        else:
            debug.debug('can not get verfiy pic')
        smsMsg = findResult['smsMsg']
        if smsMsg:
            self.pTSmsChallengeTip.setPlainText(smsMsg)
        else:
            debug.error('Can not found smsMsg %s %s'
                        % (appleId, currentTaskName))

    def getTaskResult(self, appleId):
        currentTaskName = self.appContext.getCurrentTaskName()
        results = self.reserverResult.getData(currentTaskName)
        if not results:
            debug.info('Can not find %s' % currentTaskName)
            return
        findResult = None
        for result in results:
            if appleId in result.values():
                findResult = result
        if not findResult:
            debug.error('can not found verifyData %s,%s'
                        % (appleId, currentTaskName))
            return
        return findResult

    def fillVerifyCodePic(self, verifyData):
        image = QtGui.QImage.fromData(verifyData)
        pixmap = QtGui.QPixmap(image)
        size = QSize(pixmap.width(), pixmap.height())
        # self.ui.lbVerifyCodePic
        self.lbVerifyCodePic.resize(size)
        # self.ui.lbVerifyCodePic.setPixmap(pixmap)
        self.lbVerifyCodePic.setPixmap(pixmap)

    def checking(self, statusTasks, finished):
        while statusTasks:
            for index, statusTask in enumerate(statusTasks):
                progress = str(statusTask['taskProgress'])
                appleId = statusTask['appleId']
                debug.debug('checking %s %s' % (appleId, progress))
                if progress == '100':
                    for status in finished:
                        if status['appleId'] == appleId:
                            status = dict(status, **statusTasks[index])
                    time.sleep(1)
                    self.signalStoreResult.emit(appleId)
                    time.sleep(2)
                    del statusTasks[index]
                self.signalUpdateProgress.emit(appleId, progress)
                time.sleep(3)

        debug.info('Terminal check %s' % self.appContext.getCurrentTaskName())
        self.enableStart()

    def storeResult(self, appleId):
        debug.debug('store result')
        curTask = self.appContext.getCurrentTaskName()
        for status in self.finishedAppleId:
            if status['appleId'] == appleId:
                debug.debug('save task %s %s' % (curTask, appleId))
                result = {
                    'appleId': appleId,
                    'smsMsg': status['prompInfo'],
                    'verifyCodeData': status['verifyCodeData']}
                self.reserverResult.add(curTask, result)

    def closeEvent(self, event):
        '''
        save the current task list
        '''
        return
        task = self.appContext.getCurrentTask()
        self.appContext.taskManageDLG._storeToDefault(task)

    def importTask(self):
        ret = self.appContext.tasklistDLG.exec_()
        if ret == 0:
            return
        tasks = self.appContext.tasklistDLG.getTasks()
        if tasks:
            self.fillTaskView(tasks[0])
            self.appContext.setCurrentTask(tasks[0])
        self.enableStart()

    def enableStart(self):
        self.ui.action_start_task.setEnabled(True)

    def disableStart(self):
        self.ui.action_start_task.setEnabled(False)

    def _getCurrentAppleId(self):
        row = self.preSelectedRow
        if row == -1:
            row = self.getTaskTable().currentRow()
            if row == -1:
                return
            self.preSelectedRow = row
        appleid = self.getTaskTable().item(row, 0).text()
        return appleid

    def _getCurrentTaskStatus(self):
        appleid = self._getCurrentAppleId()
        for taskstatus in self.finishedAppleId:
            if taskstatus['appleId'] == appleid:
                return taskstatus

    def refresh(self):
        # appleid = self._getCurrentAppleId()
        taskstatus = self._getCurrentTaskStatus()
        if not taskstatus:
            return
        appleid = taskstatus['appleId']
        taskstatus['verifyCodeData'] = None
        if taskstatus:
            taskstatus['taskCmd'] = 'refresh'
            time.sleep(2)
            data = taskstatus['verifyCodeData']
            counter = 3
            while not data and counter > 0:
                time.sleep(1)
                data = taskstatus['verifyCodeData']
                counter -= 1

            if data:
                self.fillVerifyCodePic(data)
                taskname = self.appContext.getCurrentTaskName()
                self.reserverResult.update(taskname, appleid,
                                           'verifyCodeData', data)
                taskstatus['verifyCodeData'] = None
            else:
                debug.info('refresh failed')
            taskstatus['taskCmd'] = None

    def selectTimeSlot(self, timeSlotId):
        '''post the timeslot data'''
        taskStatus = self._getCurrentTaskStatus()
        if taskStatus:
            taskStatus['id'] = timeSlotId
            taskStatus['taskCmd'] = 'timeslot'
            taskStatus['clientTimezone'] = 'Asia/Shanghai'
            taskStatus['cmdStatus'] = None
            timer = 30
            while not taskStatus['cmdStatus'] and timer > 0:
                time.sleep(1)
                timer -= 1
                debug.debug('check timeslot cmd status')
            if taskStatus['cmdStatus'] == 'OK':
                result = self.getTaskResult(taskStatus['appleId'])
                result['smsMsg'] = taskStatus['prompInfo']
                print(result['smsMsg'])
                self.fillResultView(taskStatus['appleId'])
            elif taskStatus['cmdStatus'] == 'NOK':
                debug.error('selected time error')
            else:
                debug.error('selectTimeSlot failed')

    def submit(self):
        taskStatus = self._getCurrentTaskStatus()
        if taskStatus:
            captcha = self.lECaptchaAnswer.text()
            taskStatus['captchaAnswer'] = str(captcha)
            phoneNumber = self.lEPhoneNumber.text()
            taskStatus['phoneNumber'] = str(phoneNumber)
            taskStatus['smsCode'] = str(self.lESmsCode.text())
            taskStatus['clientTimezone'] = 'Asia/Shanghai'
            taskStatus['countryISDCode'] = '86'
            taskStatus['cmdStatus'] = None
            taskStatus['taskCmd'] = 'submit'
            timer = 30
            while not taskStatus['cmdStatus'] and timer > 0:
                time.sleep(1)
                debug.debug('check cmdStatus')
                timer -= 1
            print('end check cmdStatus')
            if taskStatus['cmdStatus'] == 'NOK':
                debug.info('submit error')
                self.refresh()

            if taskStatus['cmdStatus'] == 'OK':
                result = taskStatus['timeSlots']
                self.fillTableWidget(result[0], result[1])
                self.showTimeSlots()
        else:
            debug.error('submit error')

    def isCmdOk(self, status):
        return status['cmdStatus'] == 'OK'

    def showTimeSlots(self):
        self.taskViewWidget.show()
        self.taskViewWidget.stackedWidget.setCurrentIndex(1)

    def viewDetail(self):
        self.taskViewWidget.show()
        self.taskViewWidget.stackedWidget.setCurrentIndex(1)
        # taskStatus = self._getCurrentTaskStatus()
        # if taskStatus:
        #     taskStatus['taskCmd'] = 'timeslot'
        #     timer = 3
        #     while not taskStatus['cmdStatus'] and timer > 0:
        #         time.sleep(1)
        #         timer -= 1
        #     if self.isCmdOk(taskStatus):
        #         ret = taskStatus['timeSlots']
        #         self.fillTableWidget(ret[0], ret[1])
