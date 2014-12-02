# -*- coding: utf-8 -*-
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from ui_newtaskdlg import Ui_NewTaskDialog
from utils import debug


class NewTaskDLG(QtGui.QDialog):

    def __init__(self, stores, reservType, parent=None):
        super(NewTaskDLG, self).__init__(parent)
        self.ui = Ui_NewTaskDialog()
        self.ui.setupUi(self)
        self.ui.combServType.addItems(reservType)
        for store in stores:
            self.ui.combStore.addItem(QtCore.QString(store))
        self.storeIndex = None
        self.storeName = None
        self.reservType = None
        self.reservIndex = None
        # 预约码
        self.reservCode = None
        self.loginData = {}

    def startTask(self):
        self.storeIndex = self.ui.combStore.currentIndex()
        self.storeName = self.ui.combStore.currentText()
        self.reservIndex = self.ui.combServType.currentIndex()
        self.reservType = self.ui.combServType.currentText()

        self.loginData['appleId'] = str(self.ui.lEUserName.text())
        self.loginData['accountPassword'] = str(self.ui.lEPasswd.text())
        self.loginData['phoneNumber'] = str(self.ui.lEPhoneNumber.text())
        self.loginData['governmentID'] = str(self.ui.lEGovId.text())
        self.loginData['governmentIDType'] = 'CN.PRCID'
        self.loginData['reservType'] = str(self.reservType)
        self.loginData['reservCode'] = str(self.ui.lEReservCode.text())
        self.loginData['storeName'] = str(self.storeName)

        isOk = True
        for key, val in self.loginData.items():
            if not val:
                debug.info('Please input %s' % key)
                isOk = False
                break
        if isOk:
            self.accept()

    def importUser(self):
        filter = "GenBar(*.usr);;All(*)"
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                                                     caption="OpenUser",
                                                     directory='.',
                                                     filter=filter)
        import shelve
        data = shelve.open(str(fileName))
        self.ui.lEUserName.setText(data['account'])
        self.ui.lEPasswd.setText(data['passwd'])
        self.ui.lEGovId.setText(data['governmentId'])
        self.ui.lEPhoneNumber.setText(data['phonenumber'])
        data.close()
