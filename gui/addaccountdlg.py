# -*- coding: utf-8 -*-
import PyQt4.QtGui as QtGui
from uidesigner.ui_accountdlg import Ui_AccountDialog
from sites.apple_genius_bar.confhelper import ConfHelper
from utils import debug


class AddAccountDLG(QtGui.QDialog):
    def __init__(self, accountfile, parent=None):
        super(AddAccountDLG, self).__init__()
        self.ui = Ui_AccountDialog()
        self.ui.setupUi(self)
        self.accountfile = accountfile

    def accept(self):
        confhelper = ConfHelper()
        appleid = str(self.ui.lEAccount.text())
        accounts = confhelper.getAccounts(self.accountfile)
        account = {}
        account['id'] = str(len(accounts)+1)
        account['appleid'] = appleid
        account['passwd'] = str(self.ui.lEPasswd.text())
        account['governmentid'] = str(self.ui.lEGovId.text())
        account['phonenumber'] = str(self.ui.lEPhoneNumber.text())
        accounts[account['id']] = account
        isOk = True
        for key, val in account.items():
            if not val:
                isOk = False
                debug.debug('Please type %s' % key)
                QtGui.QMessageBox.warning(self, "Info",
                                          "Please input %s" % key,
                                          QtGui.QMessageBox.Yes)
                break
        if isOk:
            confhelper.addAccounts(self.accountfile, accounts)
            super(AddAccountDLG, self).accept()
        else:
            debug.error('empty field')
