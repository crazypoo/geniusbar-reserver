# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog, QFileDialog
from PyQt4.QtGui import QAction
from PyQt4.QtGui import QMenu
from PyQt4.QtGui import QTableWidgetItem
from uidesigner.ui_accountmanagedlg import Ui_AccountDLG
from utils import debug
from sites.apple_genius_bar.account import Account
from functools import partial


class AccountManagerDLG(QDialog):
    def __init__(self, appContext, parent=None):
        super(AccountManagerDLG, self).__init__(parent)
        self.ui = Ui_AccountDLG()
        self.ui.setupUi(self)
        self.appContext = appContext
        self.ui.tWAccounts.signalCellContextMenu.connect(self.contextMenuEvent)
        self._initUi()

    def _addToTask(self, acount):
        self.appContext.currentTaskList.addAccount(acount)

    def contextMenuEvent(self, event):
        item = self.ui.tWAccounts.itemAt(event.pos())
        if not item:
            return
        name = str(item.text())
        selectedaccount = None
        accounts = self.appContext.accountManager.getAccounts()
        for _, account in accounts.items():
            if name == account['appleid']:
                selectedaccount = account
                break

        actfun = partial(self._addToTask, selectedaccount)
        self.act_addToTask = QAction(u'添加到任务', self, triggered=actfun)
        popMenu = QMenu()
        popMenu.addAction(self.act_addToTask)
        popMenu.exec_(self.cursor().pos())


    def _initUi(self):
        accounts = self.appContext.accountManager.getAccounts()
        self.updataAccountsTableView(accounts)

    def clear(self):
        self.ui.lEAccount.setText('')
        self.ui.lEGovId.setText('')
        self.ui.lEPhoneNumber.setText('')
        self.ui.lEPasswd.setText('')

    def addAccount(self):
        account = {}
        account['appleid'] = str(self.ui.lEAccount.text())
        account['passwd'] = str(self.ui.lEPasswd.text())
        account['governmentid'] = str(self.ui.lEGovId.text())
        account['phonenumber'] = str(self.ui.lEPhoneNumber.text())
        for key, item in account.items():
            if len(item) == 0:
                debug.debug('%s can not empty' % key)
                return

        account = Account(account)
        self.appContext.accountManager.addAccounts(account.getData())
        accounts = self.appContext.accountManager.getAccounts()
        self.updataAccountsTableView(accounts)

    def importFromFile(self):
        filter = "All(*)"
        fileName = QFileDialog.getOpenFileName(self,
                                               caption="导入账号",
                                               directory='.',
                                               filter=filter)
        if not fileName:
            return

        accounts = {}
        # 账号，密码，身份证
        with open(fileName, 'r') as f:
            for line in f.readlines():
                account = {}
                l = line.replace('\n', '').replace(' ', '').split(',')
                account['appleid'] = l[0]
                account['passwd'] = l[1]
                account['governmentid'] = l[2]
                account['phonenumber'] = ''
                accounts[l[0]] = account
        self.appContext.accountManager.addAccounts(accounts)
        accounts = self.appContext.accountManager.getAccounts()
        self.updataAccountsTableView(accounts)

    def updataAccountsTableView(self, accounts):
        rowCount = len(accounts)
        self.ui.tWAccounts.setRowCount(rowCount)
        row = 0
        for _, account in accounts.items():
            item = QTableWidgetItem()
            item.setText(account['appleid'])
            self.ui.tWAccounts.setItem(row, 0, item)

            item = QTableWidgetItem()
            item.setText(account['passwd'])
            self.ui.tWAccounts.setItem(row, 1, item)

            item = QTableWidgetItem()
            item.setText(account['governmentid'])
            self.ui.tWAccounts.setItem(row, 2, item)

            item = QTableWidgetItem()
            item.setText(account['phonenumber'])
            self.ui.tWAccounts.setItem(row, 3, item)
            row += 1
