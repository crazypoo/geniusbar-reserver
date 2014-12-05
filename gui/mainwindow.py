# -*- coding: utf-8 -*-
import os
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from uidesigner.ui_mainwindow import Ui_MainWindow
from sites.apple_main import AppleGeniusBarReservation
from taskmanagedlg import TaskManageDLG
from accountmanagedlg import AccountManagerDLG
from sites.apple_genius_bar.confhelper import AccountManager


class AppContext():
    def __init__(self):
        self.accountManagerDLG = None
        self.taskManageDLG = None
        self.proxyManagerDLG = None


class MainWindow(QtGui.QMainWindow):
    signalViewTask = QtCore.pyqtSignal(int)

    def __init__(self, abscwd, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tasks = []
        self.index = 1
        self.stores = AppleGeniusBarReservation.Init_stores_list()
        self.storelist = [store for store, url in
                          [item for index, item in self.stores.items()]]

        self.reservTypes = ["serviceType_iPhone",
                            "serviceType_iPad",
                            "serviceType_iPod",
                            "serviceType_Mac"]

        self.currentDir = abscwd
        account_dir = os.path.join(abscwd, 'res/accounts/account.dat')
        self.accountManager = AccountManager(account_dir)
        self.appContext = AppContext()
        self.accountManagerDLG = AccountManagerDLG(self.accountManager)
        self.appContext.accountManagerDLG = self.accountManagerDLG
        self.taskManageDLG = TaskManageDLG(self.appContext,
                                           abscwd,
                                           self.storelist,
                                           self.reservTypes)
        self.appContext.taskManageDLG = self.taskManageDLG

    def accountManage(self):
        self.accountManagerDLG.show()

    def taskManage(self):
        self.taskManageDLG.exec_()
