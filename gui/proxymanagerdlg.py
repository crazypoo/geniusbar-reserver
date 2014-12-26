# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog, QTableWidgetItem
from PyQt4.QtGui import QFileDialog, QRegExpValidator
from PyQt4.QtGui import QAbstractItemView, QPushButton
from PyQt4.QtCore import pyqtSignal, QRegExp
from gui.uidesigner.ui_proxymanagedlg import Ui_ProxyFinderDLG
from proxy.proxyfinder import ProxyMgr, CheckerSingle
from multiprocessing import Manager
from threading import Thread
import time
from utils import debug
from functools import partial


class ProxyManagerDLG(QDialog):
    sigUpdateProgressBar = pyqtSignal(int)
    sigFillIpTable = pyqtSignal()
    sigProxyAvaliable = pyqtSignal(int)

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
        self.mode = 0

    def setupViews(self):
        # test data
        # self.ips = [('129.0.0.1', '8080'),('221.7.112.108', '80'),('127.0.0.1', '80')]
        self.ips = []
        regExp = QRegExp ("((2[0-4]\\d|25[0-5]|[01]?\\d\\d?)\\.){3}(2[0-4]\\d|25[0-5]|[01]?\\d\\d?)")
        pValidator = QRegExpValidator(regExp)
        self.ui.lEProxyIp.setValidator(QRegExpValidator(pValidator))
        self.ui.lEProxyIp.setInputMask('000.000.000.000;')

        self.ips = self.load(self.appContext.proxyServerConfDB)
        self.fillResultTable(self.ips)

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
        self.procData['ips'] = []
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
        self.ui.tableWidget.clear()
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

    def checkWaiter(self, status):
        while not status:
            time.sleep(1)
        pass

    def isAvaliable(self, proxyServer):
        self.sender().setText(u'检查中...')
        # checker = Thread(target=CheckerSingle, args=(proxyServer[0],))
        # checker.start()
        ret = CheckerSingle(proxyServer)
        if ret:
            self.sender().setText(u'可用')
        else:
            self.sender().setText(u'不可用')

    def updateTable(self):
        self.fillResultTable(self.procData['ips'])

    def _updateProxy(self, procData):
        url = self.ui.lEProxyUrl.text()
        proxyMgr = ProxyMgr([str(url)])
        ips = proxyMgr.getAvailableProxys(procData)
        procData['ips'] = ips
        self.sigFillIpTable.emit()

    def importProxys(self):
        filter = "Prx(*.prx);;All(*)"
        fileName = QFileDialog.getOpenFileName(self,
                                               caption="导入代理",
                                               directory='./res',
                                               filter=filter)
        if not fileName:
            return

        self.ips.extend(self.load(fileName))
        self.fillResultTable(self.ips)

    def load(self, fileName):
        ips = []
        try:
            with open(fileName, 'r') as f:
                for line in f.readlines():
                    line = line.replace('\n', '').strip()
                    line = line.split(':')
                    if (not line[0]) or (not line[1]):
                        continue
                    ips.append((line[0], line[1]))
        except Exception as e:
            debug.error('%s %s' % (str(e), fileName))
        finally:
            return ips

    def addProxy(self):
        ip = self.ui.lEProxyIp.text()
        port = self.ui.lEPort.text()
        if not (ip and port):
            return
        self.ips.append((ip, port))
        self.fillResultTable(self.ips)
        debug.debug('add proxy')
        pass

    def showEvent(self, event):
        ''' '''
        print('show event')
        pass

    def closeEvent(self, event):
        '''
        restore the proxyServers
        '''
        print('close event')

    def saveIps(self):
        with open(self.appContext.proxyServerConfDB, 'w') as f:
            for ip, port in self.ips:
                f.write('%s:%s\n' % (ip, port))

    def accept(self):
        if not self.mode == 1:
            self.saveIps()
        super(ProxyManagerDLG, self).accept()

    def select(self):
        self.mode = 1  # select
        ret = self.exec_()
        if not ret == 1:
            return
        row = self.ui.tableWidget.currentRow()
        print('currentRow %s' % row)
        if row != -1:
            ip = self.ui.tableWidget.item(row, 0).text()
            port = self.ui.tableWidget.item(row, 1).text()
            prxserv = "%s:%s" % (ip, port)
            print('prxserv %s' % prxserv)
            return prxserv
