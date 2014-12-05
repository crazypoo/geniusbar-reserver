# -*- coding: utf-8 -*-
import PyQt4.QtGui as QtGui
from PyQt4.QtCore import QString
from PyQt4.QtGui import QMenu
from PyQt4.QtGui import QAction
from uidesigner.ui_taskmanagedlg import Ui_TaskManageDLG
from utils import debug
from sites.apple_genius_bar.task import Task
from functools import partial


class TaskManageDLG(QtGui.QDialog):

    def __init__(self,
                 appconext,
                 conffile,
                 stores,
                 reservType,
                 parent=None):

        super(TaskManageDLG, self).__init__(parent)
        self.ui = Ui_TaskManageDLG()
        self.ui.setupUi(self)
        self.tasks = {}
        self.conffile = conffile
        self.initUi(stores, reservType)

        self.appContext = appconext

    def initUi(self, stores, reservType):
        self.ui.cBReservType.addItems(reservType)
        # for store in stores:
        self.ui.cBStoreName.addItems(stores)
        self.ui.lEProxyIP.setText('')
        self.ui.lEProxyPort.setText('80')
        self.ui.lETaskName.setText('task1')
        self.ui.tWTasks.signalCellContextMenu.connect(self.taskCellContextMenuEvent)


    def _addAccount(self, item):
        ret = self.appContext.accountManagerDLG.exec_()
        if 0==ret:
            return

    def _deleteTaskList(self, item):
        debug.debug('_deleteTaskList')
        pass

    def taskCellContextMenuEvent(self, event):
        item = self.ui.tWTasks.itemAt(event.pos())
        if not item:
            return
        actfun = partial(self._addAccount, item)
        self.act_addAccount = QAction(u'添加账户', self, triggered=actfun)
        actfun = partial(self._addAccount, item)
        self.act_delete = QAction(u'删除', self, triggered=actfun)
        popMenu = QMenu()
        popMenu.addAction(self.act_addAccount)
        popMenu.exec_(self.cursor().pos())

    def addTask(self):
        taskName = str(self.ui.lETaskName.text())
        storeName = str(self.ui.cBStoreName.currentText())
        reservType = str(self.ui.cBReservType.currentText())
        proxyServer = str(self.ui.lEProxyIP.text())
        proxyPort = str(self.ui.lEProxyPort.text())

        task = Task(taskName, storeName,
                    reservType, proxyServer, proxyPort)

        if task.taskName not in self.tasks.keys():
            self.tasks[taskName] = task
        self.updateTaskTableWidget()

    def taskCellClicked(self, row, col):
        if 0 == col:
            item = self.ui.tWTasks.currentItem()
            task = self.tasks[str(item.text())]
            self.updataAccountsView(task.getAccounts())

    def updataAccountsView(self, accounts):
        self.ui.lWAccounts.clear()
        for account in accounts:
            self.ui.lWAccounts.addItem(account.userName)

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
            item.setText('%s:%s' % (task.proxyServer, task.proxyPort))
            self.ui.tWTasks.setItem(rowCount, 3, item)
            rowCount += 1
