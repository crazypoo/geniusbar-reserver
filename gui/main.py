import PyQt4.QtGui as QtGui
import sys
if '../' not in sys.path:
    sys.path.append('../')
import multiprocessing
from taskdlg import TaskDLG
from ui_mainwindow import Ui_MainWindow
from sites.apple_main import AppleGeniusBarReservation
stores = AppleGeniusBarReservation.Init_stores_list()



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tasks = []
        self.index = 1

    def newTask(self):
        store = stores[self.index][1]
        store_url = AppleGeniusBarReservation.Get_store_url(store)
        supporturl = AppleGeniusBarReservation.Get_suppport_url(store_url)
        taskDlg = TaskDLG(supporturl, taskId=len(self.tasks)+1, parent=self)
        taskDlg.setModal(False)
        self.tasks.append(taskDlg)
        taskDlg.show()
        self.index += 1

if __name__ == '__main__':
    #multiprocessing.freeze_support()
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
