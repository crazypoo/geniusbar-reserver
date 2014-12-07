# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialog
from uidesigner.ui_accountlistdlg import Ui_AccountListDLG


class AccountListDLG(QDialog):
    def __init__(self, appContext, parent=None):
        super(AccountListDLG, self).__init__(parent)
        self.ui = Ui_AccountListDLG()
        self.ui.setupUi(self)
        self.appContext = appContext
        self.selectedAccounts = None
        self.initUI()

    def initUI(self):
        self.ui.listWidget.clear()
        accounts = self.appContext.accountManager.getAccounts()
        for _, account in accounts.items():
            self.ui.listWidget.addItem(account['appleid'])

    def showEvent(self, event):
        self.initUI()

    def getAccounts(self):
        tmp = self.selectedAccounts
        self.selectedAccounts = []
        return tmp

    def _getAccounts(self):
        items = self.ui.listWidget.selectedItems()
        result = []
        accounts = self.appContext.accountManager.getAccounts()
        for item in items:
            appleid = str(item.text())
            for _, account in accounts.items():
                if appleid in account.values():
                    result.append(account)
                    break

        return result

    def accept(self):
        self.selectedAccounts = self._getAccounts()
        super(AccountListDLG, self).accept()
