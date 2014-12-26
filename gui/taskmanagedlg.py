# -*- coding: utf-8 -*-
import PyQt4.QtGui as QtGui
from PyQt4.QtCore import QString
from PyQt4.QtGui import QMenu
from PyQt4.QtGui import QAction
from PyQt4.QtGui import QTableWidgetItem
from uidesigner.ui_taskmanagedlg import Ui_TaskManageDLG
from utils import debug
from sites.apple_genius_bar.task import Task
from functools import partial
import cPickle as pickle
import os
import glob


class TaskManageDLG(QtGui.QDialog):

    def __init__(self,
                 appconext,
                 stores,
                 reservType,
                 parent=None):

        super(TaskManageDLG, self).__init__(parent)
        self.appContext = appconext
        self.ui = Ui_TaskManageDLG()
        self.ui.setupUi(self)
        self.tasks = {}
        self.initUi(stores, reservType)
        self.defultTask = None
        sig = self.ui.lWAccounts.signalCellContextMenu
        sig.connect(self.contextMenuEvent)

    def initUi(self, stores, reservType):
        sig = self.ui.tWTasks.signalCellContextMenu
        sig.connect(self.taskCellContextMenuEvent)

        taskfiles = self.getTaskfiles()
        self.tasks = self.getTasksFromdisk(taskfiles)
        self.setupViews()

        self.ui.cBReservType.addItems(reservType)
        # for store in stores:
        self.ui.cBStoreName.addItems(stores)
        # self.ui.lEProxyIP.setText('')
        # self.ui.lEProxyPort.setText('')
        self.ui.lETaskName.setText('task%s' % str(len(self.tasks)+1))

    def setupViews(self):
        # update twTasklist
        if self.tasks:
            self.filltWTasksView(self.tasks)
        self.setWindowIcon(QtGui.QIcon('res/img/genius_bar.png'))

    def _removeAccout(self, applid):
        row = self.ui.tWTasks.currentRow()
        item = self.ui.tWTasks.item(row, 0)
        if not item:
            return
        task = self.tasks[str(item.text())]
        task.status = 1
        for index, acount in enumerate(task.getAccounts()):
            if applid in acount.values():
                del task.accounts[index]
        self.taskCellClicked(row, 0)

    def contextMenuEvent(self, event):
        item = self.ui.lWAccounts.itemAt(event.pos())
        if not item:
            return

        actfun = partial(self._removeAccout, str(item.text()))
        self.act_delete = QAction(u'删除', self, triggered=actfun)

        popMenu = QMenu()
        popMenu.addAction(self.act_delete)
        popMenu.exec_(self.cursor().pos())

    def getTaskfiles(self):
        # get all task
        taskdir = self.appContext.getTaskStoreDir()
        taskfiles = glob.glob(os.path.join(taskdir, "*.tkl"))
        return taskfiles

    def filltWTasksView(self, tasks):

        rowCount = len(tasks)
        self.ui.tWTasks.setRowCount(rowCount)
        row = 0
        for taskname, task in tasks.items():
            item = QTableWidgetItem()
            item.setText(task.taskName)
            self.ui.tWTasks.setItem(row, 0, item)

            item = QtGui.QTableWidgetItem()
            item.setText(unicode(task.storeName))
            self.ui.tWTasks.setItem(row, 1, item)

            item = QtGui.QTableWidgetItem()
            item.setText(task.reservType)
            self.ui.tWTasks.setItem(row, 2, item)

            item = QtGui.QTableWidgetItem()
            item.setText(task.proxyServer)
            self.ui.tWTasks.setItem(row, 3, item)

            item = QtGui.QTableWidgetItem()
            item.setText(task.proxyPort)
            self.ui.tWTasks.setItem(row, 4, item)
            row += 1

    def getDefaultTask(self):
        if self.defultTask:
            return self.defultTask
        # read from dump file
        taskfile = self.appContext.getDefaultTaskFile()
        try:
            with open(taskfile, 'r') as f:
                defaultfile = f.readline().replace('\n', '')
                with open(defaultfile, 'rb') as df:
                    self.defultTask = pickle.load(df)
                return self.defultTask
        except Exception as e:
            debug.error('Error %s' % str(e))

        return None

    def _addAccount(self, task):
        ret = self.appContext.accountListDLG.exec_()
        if 0 == ret:
            return
        accounts = self.appContext.accountListDLG.getAccounts()
        if not accounts:
            return

        appleids = [account['appleid'] for account in task.accounts]
        for index, account in enumerate(accounts):
            if account['appleid'] in appleids:
                del accounts[index]

        task.accounts.extend(accounts)
        task.status = 1
        self.updataAccountsView(task.accounts)

    def _deleteTaskList(self, taskName):
        del self.tasks[taskName]
        self.updateTaskTableWidget()
        # del taskfile
        filedir = self.appContext.getTaskStoreDir()
        filedir = os.path.join(filedir, self.mkTaskListName(taskName))
        try:
            debug.debug('delete %s' % filedir)
            os.remove(filedir)
        except Exception as e:
            debug.error('Can not del %s %s' % (filedir, str(e)))

    def storeToDefault(self, task):
        if not task:
            debug.info('Info storeToDefault task is None')
            return
        try:
            dftaskfile = self.appContext.getDefaultTaskFile()
            fileName = self.mkTaskListName(task.taskName)
            debug.debug('save task %s to default' % fileName)
            taskdir = self.appContext.getTaskStoreDir()
            taskfile = os.path.join(taskdir, fileName)
            with open(dftaskfile, 'w') as f:
                f.write(taskfile)
        except Exception as e:
            debug.error('Error write %s %s' % (taskfile, str(e)))
        self.setupViews()

    def getTasksFromdisk(self, taskfiles):
        tasks = {}
        for taskfile in taskfiles:
            # debug.debug('read task from %s' % taskfile)
            try:
                with open(taskfile, 'rb') as f:
                    task = pickle.load(f)
                    tasks[task.taskName] = task
            except Exception as e:
                debug.error('Error %s' % str(e))
            finally:
                pass

        return tasks

    def mkTaskListName(self, taskname):
        return "%s.tkl" % taskname

    def saveTask(self, tasks):
        for task in tasks:
            if task.status == 0:
                continue
            fileName = self.mkTaskListName(task.taskName)
            debug.debug('save task %s' % fileName)
            taskdir = self.appContext.getTaskStoreDir()
            taskfile = os.path.join(taskdir, fileName)
            task.status = 0
            try:
                with open(taskfile, 'wb') as f:
                    pickle.dump(task, f)
            except Exception as e:
                debug.error('Error write %s %s' % (taskfile, str(e)))

    def taskCellContextMenuEvent(self, event):

        curRow = self.ui.tWTasks.currentRow()
        if curRow == -1:
            return
        taskName = self.ui.tWTasks.item(curRow, 0).text()
        taskName = str(taskName)
        #self.appContext.currentTaskList = self.tasks[taskName]

        actfun = partial(self.storeToDefault, self.tasks[taskName])
        self.act_storeTodefault = QAction(u'设置成默认', self, triggered=actfun)

        actfun = partial(self._addAccount, self.tasks[taskName])
        self.act_addAccount = QAction(u'添加账户', self, triggered=actfun)

        actfun = partial(self._deleteTaskList, taskName)
        self.act_delete = QAction(u'删除', self, triggered=actfun)

        popMenu = QMenu()
        popMenu.addAction(self.act_storeTodefault)
        popMenu.addAction(self.act_addAccount)
        popMenu.addAction(self.act_delete)
        popMenu.exec_(self.cursor().pos())

    def addTask(self):
        taskName = str(self.ui.lETaskName.text())
        storeName = str(self.ui.cBStoreName.currentText())
        reservType = str(self.ui.cBReservType.currentText())
        proxyServer = str(self.ui.lEProxyIP.text())
        proxyPort = str(self.ui.lEProxyPort.text())

        task = Task(taskName, storeName,
                    reservType, proxyServer, proxyPort)
        task.status = 1
        if task.taskName not in self.tasks.keys():
            self.tasks[taskName] = task
        self.updateTaskTableWidget()
        self.ui.lETaskName.setText('task%s' % str(len(self.tasks)+1))

    def taskCellClicked(self, row, col):
        item = self.ui.tWTasks.item(row, 0)
        if not item:
            return
        task = self.tasks[str(item.text())]
        self.updataAccountsView(task.getAccounts())

    def updataAccountsView(self, accounts):
        self.ui.lWAccounts.clear()
        for account in accounts:
            self.ui.lWAccounts.addItem(account['appleid'])

    def updateTaskTableWidget(self):
        rowCount = len(self.tasks)
        self.ui.tWTasks.setRowCount(rowCount)
        rowCount = 0
        for _, task in self.tasks.items():
            item = QtGui.QTableWidgetItem()
            item.setText(QString(task.taskName))
            self.ui.tWTasks.setItem(rowCount, 0, item)

            item = QtGui.QTableWidgetItem()
            # debug.debug(unicode(task.storeName))
            item.setText(unicode(task.storeName))
            self.ui.tWTasks.setItem(rowCount, 1, item)

            item = QtGui.QTableWidgetItem()
            item.setText(task.reservType)
            self.ui.tWTasks.setItem(rowCount, 2, item)

            item = QtGui.QTableWidgetItem()
            item.setText('%s' % task.proxyServer)
            self.ui.tWTasks.setItem(rowCount, 3, item)
            rowCount += 1

    def accept(self):
        '''
        get the task list and save it use
        '''
        tasks = [task for name, task in self.tasks.items()]
        self.saveTask(tasks)
        super(TaskManageDLG, self).accept()
