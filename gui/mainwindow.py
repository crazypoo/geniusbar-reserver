# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('..')
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from uidesigner.ui_mainwindow import Ui_MainWindow
from addaccountdlg import AddAccountDLG
from taskdlg import TaskDLG
from newtaskdlg import NewTaskDLG
from sites.apple_main import AppleGeniusBarReservation
stores = AppleGeniusBarReservation.Init_stores_list()


class MainWindow(QtGui.QMainWindow):
    signalViewTask = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tasks = []
        self.index = 1
        self.storelist = [store for store, url in
                          [item for index, item in stores.items()]]

        self.reservTypes = ["serviceType_iPhone",
                            "serviceType_iPad",
                            "serviceType_iPod",
                            "serviceType_Mac"]
        self.loginData = {}
        currentdir = os.path.abspath(os.getcwd())
        self.account_dir = os.path.join(currentdir, 'res/accounts/accounts.dat')
        self.tasksInfo = {}
        self.initTaskIdsConnection()
        self.newtaskDLG = None

    def initTaskIdsConnection(self):
        #self.ui.pBViewAccount_1.__dict__['taskid'] = '1'
        pass

    def viewTask(self):
        #self.tasksInfo[taskid].show()
        print(str(self.sender().text()).encode('GBK'))
        print(self.sender().__dict__['taskid'])

    def newTask(self):
        if not self.newtaskDLG:
            self.newtaskDLG = NewTaskDLG(self.storelist, self.reservTypes, parent=self)
            #ret = newtaskDLG.exec_()
        if not self.newtaskDLG.isVisible():
            self.newtaskDLG.show()
        else:
            self.newtaskDLG.hide()

    def newTask1(self):
        newtaskDLG = NewTaskDLG(self.storelist, self.reservTypes, parent=self)
        ret = newtaskDLG.exec_()
        if not ret:
            return
        # get the store name
        store = stores[newtaskDLG.storeIndex][1]
        store_url = AppleGeniusBarReservation.Get_store_url(store)
        supporturl = AppleGeniusBarReservation.Get_suppport_url(store_url)
        self.loginData = newtaskDLG.loginData
        taskDlg = TaskDLG(supporturl,
                          self.loginData,
                          taskId=len(self.tasks)+1,
                          parent=self)
        taskDlg.setModal(False)
        self.tasks.append(taskDlg)
        taskDlg.show()
        self.index += 1

    def addAccount(self):
        addAccountDLG = AddAccountDLG(self.account_dir)
        addAccountDLG.exec_()
