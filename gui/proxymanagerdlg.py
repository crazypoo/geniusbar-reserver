# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog, QTableWidgetItem
from PyQt4.QtCore import pyqtSignal
from gui.uidesigner.ui_proxymanagedlg import Ui_ProxyFinderDLG
from proxy.proxyfinder import ProxyFinder
from multiprocessing import Manager
from threading import Thread
import time
from utils import debug


class ProxyManagerDLG(QDialog):
    sigUpdateProgressBar = pyqtSignal(int)
    sigFillIpTable = pyqtSignal()

    def __init__(self, appcontext, parent=None):
        super(ProxyManagerDLG, self).__init__(parent)
        self.ui = Ui_ProxyFinderDLG()
        self.ui.setupUi(self)
        self.appContext = appcontext
        self.ui.lEProxyUrl.setText('http://www.proxy360.cn/Region/China')
        self.ui.progressBar.setValue(0)

        self.sigUpdateProgressBar.connect(self.updateProgressBar)
        self.sigFillIpTable.connect(self.updateTable)

    def updateProgressBar(self, progress):
        # print('update processbar')
        self.ui.progressBar.setValue(progress)

    def updateProxy(self):
        self.procData = Manager().dict()
        self.procData['progress'] = 0
        self.procData['curIndex'] = 1
        self.procData['total'] = 0

        Thread(target=self._updateProxy, args=(self.procData,)).start()
        Thread(target=self.checking, args=(self.procData, )).start()

    def checking(self, procData):
        while True:
            self.sigUpdateProgressBar.emit(procData['progress'])
            time.sleep(1)
            if procData['progress'] >= 100:
                break
        debug.info('end proxy checking')

    def fillResultTable(self, ips):
        rowCount = len(ips)
        self.ui.tableWidget.setRowCount(rowCount)
        row = 0
        for ip, port in ips:
            itemip = QTableWidgetItem()
            itemip.setText(str(ip))
            itemport = QTableWidgetItem()
            itemport.setText(str(port))

            self.ui.tableWidget.setItem(row, 0, itemip)
            self.ui.tableWidget.setItem(row, 1, itemport)

    def updateTable(self):
        self.fillResultTable(self.procData['ips'])

    def _updateProxy(self, procData):
        url = self.ui.lEProxyUrl.text()
        proxyfinder = ProxyFinder([str(url)])
        ips = proxyfinder.get_available_proxys(procData)
        procData['ips'] = ips
        self.sigFillIpTable.emit()
