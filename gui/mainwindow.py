# -*- coding: utf-8 -*-
import os
import PyQt4.QtGui as QtGui
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import QSize
from utils import debug
from uidesigner.ui_mainwindow import Ui_MainWindow
from sites.apple_main import AppleGeniusBarReservation
from taskmanagedlg import TaskManageDLG
from accountmanagedlg import AccountManagerDLG
from sites.apple_genius_bar.confhelper import AccountManager
import multiprocessing
from multiprocessing import Manager, Pool
import threading
import time


class ApplyTask(object):
    def __init__(self, loginData):
        self.loginData = loginData
        self.appleGeniusBarReservation = AppleGeniusBarReservation(loginData)
        self.enterUrl = loginData['enterUrl']

    def apply(self, taskStatus):
        return self.appleGeniusBarReservation.jump_login_page(self.enterUrl,
                                                              taskStatus)


def Reserver(applyTask, taskStatus):
    name = multiprocessing.current_process().name
    print(name)
    for i in range(6):
        taskStatus['taskProgress'] = str(i*20)
        time.sleep(1)
    return True


class ReserverResult:
    """
    save the reserv result
    """
    def __init__(self):
        self.result = {}

    def add(self, taskName, result):
        if taskName not in self.result.keys():
            self.result[taskName] = []
        self.result[taskName].append(result)

    def getData(self, taskName):
        if taskName in self.result.keys():
            return self.result[taskName]
        return None


class AppContext():
    def __init__(self):
        self.accountManagerDLG = None
        self.taskManageDLG = None
        self.proxyManagerDLG = None
        self.defaultTaskdir = None
        self.accountManager = None
        self.currentTaskList = None

    def getCurrentTask(self):
        return self.currentTaskList

    def getCurrentTaskName(self):
        if self.currentTaskList:
            return self.currentTaskList.taskName


class MainWindow(QtGui.QMainWindow):
    signalViewTask = pyqtSignal(int)
    signalUpdateProgress = pyqtSignal(str, str)
    signalStoreResult = pyqtSignal(str, str, str)
    sigUpdateCurrentId = pyqtSignal()

    def __init__(self, abscwd, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.reserverResult = ReserverResult()
        self.preSelectedRow = None
        self.store_suburl = {}
        self.storelist = []
        self.initStoreData()
        self.currentDir = abscwd
        account_dir = os.path.join(abscwd, 'res/accounts/account.dat')
        self.accountManager = AccountManager(account_dir)
        self.appContext = AppContext()

        defaulttaskdir = os.path.join(abscwd, 'res', 'task',
                                      'defaulttask.dat')

        self.appContext.defaultTaskdir = defaulttaskdir
        self.appContext.accountManager = self.accountManager
        self.accountManagerDLG = AccountManagerDLG(self.appContext)
        self.appContext.accountManagerDLG = self.accountManagerDLG
        self.taskManageDLG = TaskManageDLG(self.appContext,
                                           abscwd,
                                           self.storelist,
                                           self.reservTypes)
        self.appContext.taskManageDLG = self.taskManageDLG

        # fillTaskView
        self.appleIdToProgresscell = {}  # = {id, item}
        task = self.taskManageDLG.getDefaultTask()
        if task:
            self.appContext.currentTaskList = task
            self.fillTaskView(task)

        # the apply process
        self.applyTasks = []
        self.signalUpdateProgress.connect(self.updateProgress)
        self.signalStoreResult.connect(self.storeResult)
        self.sigUpdateCurrentId.connect(self.updateCurrentApplIdProgress)

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
        self.accountManagerDLG.exec_()

    def taskManage(self):
        self.taskManageDLG.exec_()

    def twTasklistCellClicked(self, row, col):
        if col == 0:
            item = self.ui.tWTaskList.item(row, 0)
            appleId = item.text()
            progress = self.ui.tWTaskList.item(row, 1)
            progress = progress.text()
            self.ui.progressBar.setValue(int(progress))
            if int(progress) == 100:
                self.fillResultView(appleId)

    def getTasksInfo(self):
        accounts = self.appContext.currentTaskList.getAccounts()
        storeName = self.appContext.currentTaskList.storeName
        reservType = self.appContext.currentTaskList.reservType
        suburl = self.store_suburl[unicode(storeName)]
        url = AppleGeniusBarReservation.Get_store_url(suburl)
        supportUrl = AppleGeniusBarReservation.Get_suppport_url(url)
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
            loginDatas.append(loginData)

        return loginDatas

    def startTask(self):
        loginDatas = self.getTasksInfo()
        statusTasks = []
        pool = self.getTaskPool()
        for loginData in loginDatas:
            apy = ApplyTask(loginData)
            self.applyTasks.append(apy)
            taskStatus = Manager().dict()
            taskStatus['appleId'] = loginData['appleId']
            taskStatus['taskProgress'] = '0'
            statusTasks.append(taskStatus)
            pool.apply_async(Reserver, (apy, taskStatus))

        pool.close()
        checking = threading.Thread(target=self.checking, args=(statusTasks,))
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
        self.ui.progressBar.setValue(progress)
        if progress == 100:
            print('current selected %s' % appleId)
            self.fillResultView(appleId)

    def fillResultView(self, appleId):
        currentTaskName = self.appContext.getCurrentTaskName()
        results = self.reserverResult.getData(currentTaskName)
        if not results:
            return
        findResult = None
        for result in results:
            if appleId in result.values():
                findResult = result
        if not findResult:
            debug.error('can not found verifyData %s,%s'
                        % (appleId, currentTaskName))
        verifyData = findResult['verifyData']
        if verifyData:
            image = QtGui.QImage.fromData(verifyData)
            pixmap = QtGui.QPixmap(image)
            size = QSize(pixmap.width(), pixmap.height())
            self.ui.lbVerifyCodePic.resize(size)
            self.ui.lbVerifyCodePic.setPixmap(pixmap)
        else:
            debug.info('verifyData is none')
        smsMsg = result['smsMsg']
        if smsMsg:
            self.ui.pTSmsChallengeTip.setPlainText(smsMsg)
        else:
            debug.error('Can not found smsMsg %s %s'
                        % (appleId, currentTaskName))

    def checking(self, statusTasks):
        while statusTasks:
            for index, statusTask in enumerate(statusTasks):
                progress = statusTask['taskProgress']
                appleId = statusTask['appleId']
                print('checking %s %s' % (appleId, progress))
                self.signalUpdateProgress.emit(appleId, progress)
                time.sleep(1)
                if progress == '100':
                    smsmsg = 'hello user'#statusTask['prompInfo']
                    pic = 'this is pic'#statusTask['verifyCodeData']
                    self.signalStoreResult.emit(appleId, smsmsg, pic)
                    del statusTasks[index]
            self.sigUpdateCurrentId.emit()
        print('terminal checking')

    def storeResult(self, appleId, smsMsg,  verifyData):
        curTask = self.appContext.getCurrentTaskName()
        debug.debug('save task %s %s' % (curTask, appleId))
        result = {
            'appleId': appleId,
            'smsMsg': smsMsg,
            'verifyData': verifyData}
        self.reserverResult.add(curTask, result)
