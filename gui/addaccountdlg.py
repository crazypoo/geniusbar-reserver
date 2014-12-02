# -*- coding: utf-8 -*-
import PyQt4.QtGui as QtGui
from ui_accountdlg import Ui_AccountDialog
from utils import debug
import dbhash
import shelve
import os


class AddAccountDLG(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AddAccountDLG, self).__init__()
        self.ui = Ui_AccountDialog()
        self.ui.setupUi(self)

    def accept(self):
        debug.info('enter accept')

        account = str(self.ui.lEAccount.text())
        # accountId = str(len(self.db.items()))
        if not os.path.exists('accounts'):
            os.mkdir('accounts')
            debug.info('create accounts')
        try:
            item = shelve.open('accounts/%s.usr' % account.split('@')[0])
            item['account'] = account
            item['passwd'] = str(self.ui.lEPasswd.text())
            item['governmentId'] = str(self.ui.lEGovId.text())
            item['phonenumber'] = str(self.ui.lEPhoneNumber.text())
            isOk = True
            for key, val in item.items():
                if not val:
                    isOk = False
                    debug.debug('Please type %s' % key)
                    break
                item.close()
                if isOk:
                    debug.info('exit accept')
                    debug.debug('accept')
                    super(AddAccountDLG, self).accept()
                else:
                    debug.error('empty field')
        except Exception as e:
            debug.info('exit accept without %s' % str(e))
