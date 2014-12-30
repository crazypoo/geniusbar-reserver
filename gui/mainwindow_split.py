# -*- coding: utf-8 -*-
import os
import PyQt4.QtGui as QtGui
from PyQt4.QtGui import QSplitter, QLabel, QAction, QIcon, QMenu
from PyQt4.QtCore import QSize, Qt, QString, pyqtSignal
from utils import debug  # , WriteVerifyPic
from uidesigner.ui_mainwindow_splitter import Ui_MainWindow
from uidesigner import taskviewwidget
from sites.apple_main import AppleGeniusBarReservation
from taskmanagedlg import TaskManageDLG
from tasklistdlg import TaskListDLG
from accountmanagedlg import AccountManagerDLG
from accountlistdlg import AccountListDLG
from sites.apple_genius_bar.confhelper import AccountManager
from proxymanagerdlg import ProxyManagerDLG
import multiprocessing
from multiprocessing import Manager, Pool
import threading
import time
from tablewidget import TableWidget
from functools import partial
from PyQt4.QtGui import QFileDialog


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

    def stopAllTask(self):
        for taskname, result in self.result.items():
            for r in result:
                r['cmdTask'] = 'end'
        self.result = {}

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
        self.proxyManagerDLG = None
        self.proxyServerConfDB = None
        self.mainWindow = mainWindow
        self.reservInfodir = None

    def getDefaultTaskFile(self):
        return os.path.join(self.configurefileDir,
                            'res/task',
                            'defaulttask')

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
        self.signalCellContextMenu.connect(self.taskWidgetContextMenu)

    def taskWidgetContextMenu(self, event):
        curRow = self.taskTableWidget.currentRow()
        if curRow == -1:
            debug.info('taskWidgetContextMenu clicked %s' % curRow)
            actfun = partial(self.refreshCurTask)
            self.act_refreshtask = QAction(u'刷新', self, triggered=actfun)
            popMenu = QMenu()
            popMenu.addAction(self.act_refreshtask)
            popMenu.exec_(self.cursor().pos())
            return
        # context menus
        actfun = partial(self.changeProxyServer)
        self.act_chgprx = QAction(u'更改代理', self, triggered=actfun)
        popMenu = QMenu()
        popMenu.addAction(self.act_chgprx)

        actfun = partial(self.cancelProxyServer)
        self.act_cancelprx = QAction(u'取消代理', self, triggered=actfun)
        popMenu = QMenu()

        actfun = partial(self.refreshCurTask)
        self.act_refreshtask = QAction(u'刷新', self, triggered=actfun)
        popMenu = QMenu()

        popMenu.addAction(self.act_refreshtask)
        popMenu.addAction(self.act_chgprx)
        popMenu.addAction(self.act_cancelprx)
        popMenu.exec_(self.cursor().pos())

    def refreshCurTask(self):
        task = self.appContext.getCurrentTask()
        if task:
            self.fillTaskView(task)

    def cancelProxyServer(self):
        self.updateCurPrx('')

    def updateCurPrx(self, prxServer):
        curRow = self.taskTableWidget.currentRow()
        appleId = self.taskTableWidget.itemAt(curRow, 0).text()
        debug.debug('change prxserv %s' % appleId)
        task = self.appContext.getCurrentTask()
        ac, _ = task.getAccount(appleId)
        ac['proxyserver'] = prxServer
        item = QtGui.QTableWidgetItem()
        item.setText(prxServer)
        self.taskTableWidget.setItem(curRow, 2, item)
        self.appContext.taskManageDLG.saveTask([task])
        debug.debug('update %s, prx: %s' % (appleId, prxServer))

    def changeProxyServer(self):
        prxServer = self.appContext.proxyManagerDLG.select()
        if not prxServer:
            return
        self.updateCurPrx(prxServer)

    def setupResultTable(self):
        headers = [
            u'账号',
            u'预约信息',
            u'日期'
            ]
        self.reservResultTable = TableWidget(headers=headers)

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

    def contextMenuEvent(self, event):
        print('main window contextMenuEvent')

    def setupViews2(self):
        self.setupTaskTable()
        msplitter = QSplitter(Qt.Horizontal)
        msplitter.addWidget(self.taskTableWidget)

        rsplitter = QSplitter(Qt.Vertical, msplitter)
        self.setupResultTable()
        rsplitter.addWidget(self.reservResultTable)
        self.taskViewWidget = taskviewwidget.TaskViewWidget()
        rsplitter.addWidget(self.taskViewWidget)

        self.setCentralWidget(msplitter)
        self.msgLabel = QLabel()
        self.statusBar().addWidget(self.msgLabel)

        self.setWindowIcon(QtGui.QIcon('res/img/genius_bar.png'))

    def setupMenubar(self):
        self.act_save = QAction(QIcon('res/img/save.png'),
                                "&Save result",
                                self, statusTip='save result')
        self.act_save.triggered.connect(self.saveReservData)
        self.ui.toolBarApp.addAction(self.act_save)

        self.act_start = QAction(QIcon('res/img/start.png'),
                                 "&Start",
                                 self, statusTip='start task')

        self.act_start.triggered.connect(self.startTask)
        self.ui.toolBar.addAction(self.act_start)
        self.act_import_task = QAction(QIcon('res/img/import.png'),
                                       "&Import",
                                       self,
                                       statusTip='import task')
        self.act_import_task.triggered.connect(self.importTask)
        self.ui.toolBar.addAction(self.act_import_task)

        self.act_acntmgr = QAction(QIcon('res/img/acutmrg.png'),
                                   "&Accounts",
                                   self, statusTip='Accounts manager')

        self.act_taskmgr = QAction(QIcon('res/img/tskmgr.png'),
                                   "&Tasks",
                                   self, statusTip='tasks manager')
        self.act_proxymgr = QAction(QIcon('res/img/proxymgr.png'),
                                    "&ProxyManage",
                                    self, statusTip='proxy manage')
        self.act_proxymgr.triggered.connect(self.proxyMgr)
        self.act_acntmgr.triggered.connect(self.accountManage)
        self.act_taskmgr.triggered.connect(self.taskManage)
        self.ui.toolBarMgr.addAction(self.act_taskmgr)
        self.ui.toolBarMgr.addAction(self.act_acntmgr)
        self.ui.toolBarMgr.addAction(self.act_proxymgr)

    def __init__(self, abscwd, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupViews2()
        self.setupMenubar()
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
        self.appContext.proxyServerConfDB = 'res/prxconf/proxyserver.prx'
        self.appContext.reservInfodir = 'res/reserv'
        self.appContext.proxyManagerDLG = ProxyManagerDLG(self.appContext)
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
        self.stores = None
        self.reservTypes = ["serviceType_iPhone",
                            "serviceType_iPad",
                            "serviceType_iPod",
                            "serviceType_Mac"]

        initer = threading.Thread(target=self.doInitStoreData, args=())
        initer.start()
        initer.join(timeout=20)
        if not self.stores:
            self.statusBar().showMessage(u'读取网站信息失败请重试')

    def doInitStoreData(self):
        # the store name of each url
        self.stores = AppleGeniusBarReservation.Init_stores_list()
        for index, item in self.stores.items():
            self.store_suburl[item[0]] = item[1]
            self.storelist.append(item[0])

    def updateCurrentTaskInfo(self):
        '''
        account id and proxyserver
        '''
        rowCount = self.taskTableWidget.rowCount()
        if 0 == rowCount:
            return
        task = self.appContext.getCurrentTask()
        accounts = task.getAccounts()
        ret = {}
        for row in range(rowCount):
            appleId = self.taskTableWidget.item(row, 0).text()
            proxyServer = self.taskTableWidget.item(row, 2).text()
            ret[str(appleId)] = str(proxyServer)
        for index, account in enumerate(accounts):
            accounts[index]['proxyserver'] = ret[account['appleid']]
        task.setAccounts(accounts)

        self.appContext.setCurrentTask(task)

    def fillTaskView(self, task):

        accounts = task.getAccounts()
        rowCount = len(accounts)
        if rowCount is not 0:
            self.preSelectedRow = 0

        # self.ui.gBListName.setTitle(unicode(task.taskName))
        self.taskTableWidget.setRowCount(rowCount)
        row = 0
        for account in accounts:
            item = QtGui.QTableWidgetItem()
            item.setText(account['appleid'])
            self.taskTableWidget.setItem(row, 0, item)

            item = QtGui.QTableWidgetItem()
            item.setText("0")
            self.taskTableWidget.setItem(row, 1, item)
            self.appleIdToProgresscell[account['appleid']] = item
            item = QtGui.QTableWidgetItem()

            if 'proxyserver' not in account.keys():
                account['proxyserver'] = ''

            tmpserver = account['proxyserver']
            if not tmpserver:
                if task.proxyServer:
                    tmpserver = task.proxyServer+':'+task.proxyPort
                    account['proxyserver'] = tmpserver

            item.setText(tmpserver)
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

    def proxyMgr(self):

        self.appContext.proxyManagerDLG.show()

    def taskManage(self):
        if 1 == self.taskManageDLG.exec_():
            self.refreshCurTask()
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
        self.updateCurrentTaskInfo()
        task = self.appContext.getCurrentTask()
        if not task:
            return
        accounts = task.getAccounts()
        if not accounts:
            return
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
            loginData['proxyServer'] = account['proxyserver']
            loginDatas.append(loginData)

        return loginDatas

    def startTask(self):
        self.reserverResult.stopAllTask()
        if self.running:
            return
        self.disableStart()
        geniusBar = True
        loginDatas = self.getTasksInfo(geniusBar=geniusBar)
        if not loginDatas:
            return
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
            if loginData['proxyServer']:
                taskStatus['proxyServer'] = loginData['proxyServer']
            else:
                taskStatus['proxyServer'] = None

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
        self.twTasklistCellClicked(0, 0)

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
                # debug.debug('checking %s %s' % (appleId, progress))
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

    def exit(self):
        self.close()

    def closeEvent(self, event):
        '''
        save the current task list
        '''
        task = self.appContext.getCurrentTask()
        self.appContext.taskManageDLG.storeToDefault(task)

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
        self.running = False

    def disableStart(self):
        self.ui.action_start_task.setEnabled(False)
        self.running = True

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

            if taskStatus['cmdStatus'] == 'OK':
                # result = self.getTaskResult(taskStatus['appleId'])
                self.addReservResult(taskStatus['appleId'],
                                     taskStatus['prompInfo'])
            elif taskStatus['cmdStatus'] == 'NOK':
                debug.error('selected time error')
            else:
                debug.error('selectTimeSlot failed')

    def addReservResult(self, appleId, info):
        row = self.reservResultTable.ui.tableWidget.rowCount()+1
        self.reservResultTable.ui.tableWidget.setRowCount(row)
        accountitem = QtGui.QTableWidgetItem()
        accountitem.setText(QString(appleId))
        item = QtGui.QTableWidgetItem()
        item.setText(QString(info))
        self.reservResultTable.ui.tableWidget.setItem(row-1, 0, accountitem)
        self.reservResultTable.ui.tableWidget.setItem(row-1, 1, item)
        timestr = time.strftime('%Y:%m:%d', time.localtime(time.time()))
        item = QtGui.QTableWidgetItem()
        item.setText(QString(timestr))
        self.reservResultTable.ui.tableWidget.setItem(row-1, 2, item)

    def saveReservData(self):
        fileName = time.strftime('%Y%m%d%H%I%M.rsv',
                                 time.localtime(time.time()))
        tmpdir = os.path.join(self.appContext.reservInfodir, fileName)
        debug.debug('Save %s' % tmpdir)
        self.doSaveReservInfo(tmpdir)

    def saveAsReservData(self):
        filter = "Rev(*.rsv);;All(*)"
        fileName = QFileDialog.getSaveFileName(self,
                                               caption=u"另存为...",
                                               directory='./res',
                                               filter=filter)
        if not fileName:
            return
        self.doSaveReservInfo(fileName)

    def doSaveReservInfo(self, fileName):
        rowCount = self.reservResultTable.ui.tableWidget.rowCount()
        if rowCount == 0:
            debug.debug('No data have saved')
            return
        tw = self.reservResultTable.ui.tableWidget
        with open(fileName, 'w') as f:
            for i in range(rowCount):
                appleId = tw.item(i, 0).text()
                reserInfo = tw.item(i, 1).text()
                dt = tw.item(i, 2).text()
                f.write('%s;%s;%s\n' % (appleId, reserInfo, dt))

    def fillReservDataView(self, data):
        tw = self.reservResultTable.ui.tableWidget
        tw.clear()
        tw.setRowCount(len(data))
        for row, d in enumerate(data):
            item = QtGui.QTableWidgetItem()
            item.setText(QString(d[0]))
            tw.setItem(row, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(QString(d[1]))
            tw.setItem(row, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText(QString(d[2]))
            tw.setItem(row, 2, item)

    def loadReservData(self, filename):
        reserdata = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.replace('\n', '').split(';')
                reserdata.append(line)
        return reserdata

    def viewReservInfo(self):
        filter = "Rev(*.rsv);;All(*)"
        fileName = QFileDialog.getOpenFileName(self,
                                               caption=u"查看",
                                               directory='./res',
                                               filter=filter)
        if not fileName:
            return
        data = self.loadReservData(fileName)
        self.fillReservDataView(data)

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
                timer -= 1

            if taskStatus['cmdStatus'] == 'NOK':
                debug.info('submit error')
                debug.info(taskStatus['prompInfo'])
                self.refresh()

            elif taskStatus['cmdStatus'] == 'OK':
                result = taskStatus['timeSlots']
                self.fillTableWidget(result[0], result[1])
                self.showTimeSlots(1)
            else:
                debug.error('submit task error')

        else:
            debug.error('submit error')

    def isCmdOk(self, status):
        return status['cmdStatus'] == 'OK'

    def showTimeSlots(self, index=1):
        self.taskViewWidget.show()
        self.taskViewWidget.stackedWidget.setCurrentIndex(index)

    def showTaskResult(self, index=0):
        self.taskViewWidget.show()
        self.taskViewWidget.stackedWidget.setCurrentIndex(index)

    def viewDetail(self):
        self.taskViewWidget.show()
        if self.taskViewWidget.stackedWidget.currentIndex() == 0:
            self.taskViewWidget.stackedWidget.setCurrentIndex(1)
        else:
            self.taskViewWidget.stackedWidget.setCurrentIndex(1)
