# -*- coding: utf-8 -*-
import os
import PyQt4.QtGui as QtGui
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import QSize
from utils import debug
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

    def apply(self, taskStatus, namespace=None):
        debug.debug('start %s' % taskStatus['appleId'])
        return self.reser.Jump_login_page(self.enterUrl,
                                          taskStatus, namespace)


def Reserver(applyTask, taskStatus, namespace=None):
    name = multiprocessing.current_process().name
    debug.debug(name)
    return applyTask.apply(taskStatus, namespace)


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

    def __init__(self, abscwd, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.appContext = AppContext(abscwd)
        self.reserverResult = ReserverResult()
        self.preSelectedRow = None
        self.store_suburl = {}
        self.storelist = []
        self.initStoreData()
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

        # fillTaskView
        self.appleIdToProgresscell = {}  # = {id, item}
        task = self.taskManageDLG.getDefaultTask()
        if task:
            self.appContext.setCurrentTask(task)
            self.fillTaskView(task)

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

    def lbpicLinkActived(self, msg):
        print('actived %s' % msg)

    def lbpicLinkHovered(self, msg):
        print('howved %s' % msg)

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
        self.appContext.accountManagerDLG.exec_()
        # TODO:

    def taskManage(self):
        self.taskManageDLG.exec_()
        # TODO:
        #check the action of taskmanager, 

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
        taskName = self.ui.gBListName.title()
        task = self.appContext.taskManageDLG.tasks[str(taskName)]
        accounts = task.getAccounts()
        storeName = task.storeName
        reservType = task.reservType
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
            #loginData['cookie'] = self.createOpener()
            loginDatas.append(loginData)

        return loginDatas

    def createOpener(self):
        import urllib2
        cookie = cookielib.CookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookie_support)
        return opener

    def startTask(self):
        loginDatas = self.getTasksInfo()
        self.statusTasks = []
        self.handler = []
        pool = self.getTaskPool()
        for loginData in loginDatas:
            apy = ApplyTask(loginData)
            self.applyTasks.append(apy)
            taskStatus = Manager().dict()
            taskStatus['prompInfo'] = ''
            taskStatus['verifyCodeData'] = ''
            taskStatus['appleId'] = loginData['appleId']
            taskStatus['verifyPage'] = ''
            taskStatus['taskProgress'] = '0'
            self.statusTasks.append(taskStatus)
            # namespace = Manager().Namespace()
            # namespace.value = self.createOpener()
            # self.handler.append({loginData['appleId']: namespace})
            pool.apply_async(Reserver, (apy, taskStatus))
        pool.close()
        debug.debug('have %s task' % len(self.statusTasks))
        checking = threading.Thread(target=self.checking,
                                    args=(self.statusTasks,))
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
            time.sleep(1)
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
            return
        verifyData = findResult['verifyCodeData']
        if verifyData:
            self.fillVerifyCodePic(verifyData)
        else:
            debug.debug('can not get verfiy pic')
        smsMsg = findResult['smsMsg']
        if smsMsg:
            self.ui.pTSmsChallengeTip.setPlainText(smsMsg)
        else:
            debug.error('Can not found smsMsg %s %s'
                        % (appleId, currentTaskName))

    def fillVerifyCodePic(self, verifyData):
        image = QtGui.QImage.fromData(verifyData)
        pixmap = QtGui.QPixmap(image)
        size = QSize(pixmap.width(), pixmap.height())
        self.ui.lbVerifyCodePic.resize(size)
        self.ui.lbVerifyCodePic.setPixmap(pixmap)

    def checking(self, statusTasks):
        while statusTasks:
            for index, statusTask in enumerate(statusTasks):
                progress = str(statusTask['taskProgress'])
                appleId = statusTask['appleId']
                print('checking %s %s' % (appleId, progress))
                self.signalUpdateProgress.emit(appleId, progress)
                time.sleep(3)
                if progress == '100':
                    self.signalStoreResult.emit(appleId)
                    time.sleep(2)
                    del statusTasks[index]

            self.sigUpdateCurrentId.emit()
        print('terminal checking')

    def storeResult(self, appleId):
        curTask = self.appContext.getCurrentTaskName()
        debug.debug('save task %s %s' % (curTask, appleId))
        for status in self.statusTasks:
            if status['appleId'] == appleId:
                result = {
                    'appleId': appleId,
                    'smsMsg': status['prompInfo'],
                    'verifyCodeData': status['verifyCodeData'],
                    'verifyPage': status['verifyPage']}
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

    def refresh(self):
        row = self.ui.tWTaskList.currentRow()
        if row == -1:
            return
        appleid = self.ui.tWTaskList.item(row, 0).text()
        print('appleid %s' % appleid)
        task = self.appContext.getCurrentTask()
        # get task results
        data = self.reserverResult.getData(task.taskName)
        for taskinfo in data:
            if appleid in taskinfo.values():
                page = taskinfo['verifyPage']
                print(page)
                #page.init_cookie(taskinfo['opener'])
                #picdata = page.get_verification_code_pic()
               # print(picdata)
                #self.fillVerifyCodePic(picdata)

    def submit(self):
        print('submit')
