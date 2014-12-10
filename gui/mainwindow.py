# -*- coding: utf-8 -*-
import os
import PyQt4.QtGui as QtGui
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import QSize
from utils import debug, WriteVerifyPic
from uidesigner.ui_mainwindow import Ui_MainWindow
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


class ApplyTask(object):
    def __init__(self, loginData):
        self.loginData = loginData
        self.reser = AppleGeniusBarReservation(loginData)
        self.enterUrl = loginData['enterUrl']

    def apply(self, taskStatus):
        debug.debug('start %s' % taskStatus['appleId'])
        return self.reser.Jump_login_page(self.enterUrl,
                                          taskStatus)


def Reserver(applyTask, taskStatus):
    name = multiprocessing.current_process().name
    debug.debug(name)
    return applyTask.apply(taskStatus)


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
    def __init__(self, cwd):
        self.configurefileDir = cwd
        self.accountManagerDLG = None
        self.taskManageDLG = None
        self.tasklistDLG = None
        self.proxyManagerDLG = None
        self.accountManager = None
        self.currentTaskList = None
        self.accountListDLG = None

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

    def setCurrentTask(self, task):
        self.currentTaskList = task

    def getCurrentTaskName(self):
        if self.currentTaskList:
            return self.currentTaskList.taskName


class MainWindow(QtGui.QMainWindow):
    signalViewTask = pyqtSignal(int)
    signalUpdateProgress = pyqtSignal(str, str)
    signalStoreResult = pyqtSignal(str)
    sigUpdateCurrentId = pyqtSignal()
    sigUpdateProgressBar = pyqtSignal(str)

    def __init__(self, abscwd, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.appContext = AppContext(abscwd)
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
        self.signalUpdateProgress.connect(self.updateProgress)
        self.signalStoreResult.connect(self.storeResult)
        self.sigUpdateCurrentId.connect(self.updateCurrentApplIdProgress)
        # self.sigUpdateProgressBar.connect(self.updateProgressBar)
        # fillTaskView
        self.appleIdToProgresscell = {}  # = {id, item}
        task = self.taskManageDLG.getDefaultTask()
        if task:
            self.appContext.setCurrentTask(task)
            self.fillTaskView(task)

        self.ui.widget.sigRefresh.connect(self.refresh)
        self.ui.widget.sigSubmit.connect(self.submit)
        self.ui.widget.hide()

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

        self.ui.gBListName.setTitle(unicode(task.taskName))
        self.ui.tWTaskList.setRowCount(rowCount)
        row = 0
        for count in accounts:
            item = QtGui.QTableWidgetItem()
            item.setText(count['appleid'])
            self.ui.tWTaskList.setItem(row, 0, item)

            item = QtGui.QTableWidgetItem()
            item.setText("0")
            self.ui.tWTaskList.setItem(row, 1, item)
            self.appleIdToProgresscell[count['appleid']] = item
            item = QtGui.QTableWidgetItem()
            item.setText(task.proxyServer)
            self.ui.tWTaskList.setItem(row, 2, item)

            item = QtGui.QTableWidgetItem()
            item.setText(unicode(task.storeName))
            self.ui.tWTaskList.setItem(row, 3, item)

            item = QtGui.QTableWidgetItem()
            item.setText(task.reservType)
            self.ui.tWTaskList.setItem(row, 4, item)
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
        #check the action of taskmanager, 

    def twTasklistCellClicked(self, row, col):
        self.ui.widget.show()
        if col == 0:
            item = self.ui.tWTaskList.item(row, 0)
            appleId = item.text()
            progress = self.ui.tWTaskList.item(row, 1)
            progress = progress.text()
            self.progressBar.setValue(int(progress))
            account = self.appContext.accountManager.getAccount(appleId)
            if account:
                self.lEPhoneNumber.setText(account['phonenumber'])
            if int(progress) == 100:
                self.fillResultView(appleId)
        self.preSelectedRow = row

    def getTasksInfo(self):
        taskName = self.ui.gBListName.title()
        task = self.appContext.taskManageDLG.tasks[str(taskName)]
        accounts = task.getAccounts()
        storeName = task.storeName
        reservType = task.reservType
        suburl = self.store_suburl[unicode(storeName)]
        storeUrl = AppleGeniusBarReservation.Get_store_url(suburl)
        supportUrl = AppleGeniusBarReservation.Get_suppport_url(storeUrl)
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
            loginData['enterUrl'] = supportUrl
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
        self.ui.widget.show()
        self.twTasklistCellClicked(0, 0)
        self.running = True
        self.disableStart()
        loginDatas = self.getTasksInfo()
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
            self.statusTasks.append(taskStatus)

            taskResult = Manager().dict()
            taskResult['appleId'] = loginData['appleId']
            self.finishedAppleId.append(taskStatus)

            pool.apply_async(Reserver, (apy, taskStatus))

        pool.close()
        debug.debug('have %s task' % len(self.statusTasks))
        checking = threading.Thread(target=self.checking,
                                    args=(self.statusTasks,
                                          self.finishedAppleId))
        checking.start()

    def updateProgress(self, appleId, progress):
        item = self.appleIdToProgresscell[str(appleId)]
        item.setText(progress)
        self.updateCurrentApplIdProgress()

    def updateCurrentApplIdProgress(self):
        rowindex = self.ui.tWTaskList.currentRow()
        if rowindex == -1:
            if self.preSelectedRow:
                rowindex = self.preSelectedRow
            else:
                rowindex = 0
        self.preSelectedRow = rowindex

        appleIdItem = self.ui.tWTaskList.item(rowindex, 0)
        appleId = appleIdItem.text()
        progressItem = self.ui.tWTaskList.item(rowindex, 1)
        progress = int(progressItem.text())
        # self.getProcessBar().setValue(progress)
        self.progressBar.setValue(progress)
        if progress == 100:
            self.fillResultView(appleId)
            time.sleep(1)

    def __getattr__(self, name):
        return getattr(self.ui.widget, name)

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

            self.sigUpdateCurrentId.emit()
        debug.info('Terminal task %s' % self.appContext.getCurrentTaskName())

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
            row = self.ui.tWTaskList.currentRow()
            if row == -1:
                return
            self.preSelectedRow = row
        appleid = self.ui.tWTaskList.item(row, 0).text()
        return appleid

    def _getCurrentTaskStatus(self):
        appleid = self._getCurrentAppleId()
        for taskstatus in self.finishedAppleId:
            if taskstatus['appleId'] == appleid:
                return taskstatus

    def refresh(self):
        appleid = self._getCurrentAppleId()
        taskstatus = self._getCurrentTaskStatus()
        if not taskstatus:
            return
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
            taskStatus['taskCmd'] = 'submit'
            while not taskStatus['cmdStatus']:
                time.sleep(1)
            if taskStatus['cmdStatus'] == 'NOK':
                debug.info('submit error')
                self.refresh()
        else:
            debug.error('submit error')
        #self.enableStart()

    def viewDetail(self):
        if 0 == self.stackedWidget.currentIndex():
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)
