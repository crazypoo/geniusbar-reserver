# -*- coding: utf-8 -*-
import PyQt4.QtGui as QtGui
import sys
if '../' not in sys.path:
    sys.path.append('../')
reload(sys)
sys.setdefaultencoding('utf-8')
from utils import debug
debug.setLevel(10)
from addaccountdlg import AddAccountDLG
from taskdlg import TaskDLG
from newtaskdlg import NewTaskDLG
from ui_mainwindow import Ui_MainWindow
from sites.apple_main import AppleGeniusBarReservation
from multiprocessing import freeze_support


stores = AppleGeniusBarReservation.Init_stores_list()


class MainWindow(QtGui.QMainWindow):
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

    def newTask(self):
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
        addAccountDLG = AddAccountDLG()
        addAccountDLG.exec_()

if __name__ == '__main__':
    freeze_support()
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
