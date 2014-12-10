import time
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QMainWindow, QDialog
from PyQt4.QtCore import QUrl, QString, QObject

from utils.webpageq import WebPageQ
from uidesigner.ui_mainwindow import Ui_MainWindow
from PyQt4.QtCore import pyqtSignal
from multiprocessing import Manager, Pool
import multiprocessing
from uidesigner.taskviewwidget import TaskViewWidget


headers = {}
headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
headers["Connection"] = 'keep-alive'


class MainWindow(QMainWindow):
    def __init__(self, abscwd, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # print(text)
    def getTaskPool(self):
        poolSize = multiprocessing.cpu_count() * 2
        return Pool(processes=poolSize)

    def submit(self):
        pass
    def showEvent(self, event):
        pass
    #self.ui.widget.show()
    def reserver(self, reservInfo):
        pass

    def startTask(self):

        p = multiprocessing.Process(target=self.ui.widget.open, args=())
        p.start()
        return
        if self.ui.widget.isVisible():
            self.ui.widget.hide()
        else:
            self.ui.widget.show()
        pass
    def refresh(self):
        pass
    def accountManage(self):
        pass
        # TODO:
    def importTask(self):
        task1 = TaskViewWidget(self)
        task1.ui.lEPhoneNumber.setText('Task1')
        self.ui.widget.hide()
        task1.rect = self.ui.widget.rect
        self.ui.widget = task1
        task1.show()
        pass

    def twTasklistCellClicked(self, row, col):
        pass
    def taskManage(self):
        pass
