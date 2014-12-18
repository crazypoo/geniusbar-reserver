# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog, QTableWidgetItem
from PyQt4.QtGui import QAbstractItemView, QPushButton
from PyQt4.QtCore import pyqtSignal
from gui.uidesigner.ui_proxymanagedlg import Ui_ProxyFinderDLG
from proxy.proxyfinder import ProxyFinder
from multiprocessing import Manager
from threading import Thread
import time
from utils import debug
from functools import partial


class ProxyManagerDLG(QDialog):
    sigUpdateProgressBar = pyqtSignal(int)
    sigFillIpTable = pyqtSignal()

    def __init__(self, appcontext, parent=None):
        super(ProxyManagerDLG, self).__init__(parent)
        self.ui = Ui_ProxyFinderDLG()
        self.ui.setupUi(self)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.appContext = appcontext
        self.ui.lEProxyUrl.setText('http://www.proxy360.cn/Region/China')
        self.ui.progressBar.setValue(0)

        self.sigUpdateProgressBar.connect(self.updateProgressBar)
        self.sigFillIpTable.connect(self.updateTable)
        self.sigCellContextMenu.connect(self.cellContextMenu)
        self.setupViews()

    def setupViews(self):
        # test data
        ips = [('129.0.0.1', '8080'), ('127.0.1.1', '80')]
        self.fillResultTable(ips)

    def __getattr__(self, name):
        return getattr(self.ui.tableWidget, name)

    def cellContextMenu(self, event):
        row = self.currentRow()
        print('current row %s' % row)

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
            btitem = QPushButton()
            btitem.setText(u'检查')
            self.setCellWidget(row, 3, btitem)
            actfun = partial(self.isAvaliable, (ip, port))
            btitem.clicked.connect(actfun)
            row += 1

    def isAvaliable(self, proxyServer):
        print('isAvaliable %s %s' % proxyServer)
        self.sender().setText(u'检查中...')

    def updateTable(self):
        self.fillResultTable(self.procData['ips'])

    def _updateProxy(self, procData):
        url = self.ui.lEProxyUrl.text()
        proxyfinder = ProxyFinder([str(url)])
        ips = proxyfinder.get_available_proxys(procData)
        procData['ips'] = ips
        self.sigFillIpTable.emit()
