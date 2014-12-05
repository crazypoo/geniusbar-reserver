from PyQt4.QtGui import QDialog
from uidesigner.ui_accountmanagedlg import Ui_AccountDLG
from utils import debug


class AccountManagerDLG(QDialog):
    def __init__(self, accountManager, parent=None):
        super(AccountManagerDLG, self).__init__(parent)
        self.ui = Ui_AccountDLG()
        self.ui.setupUi(self)
        self.accountManager = accountManager
        # self.accountManager.addAccounts({'appleId': 'zhonghui944oe@163.com',
        #                                  'passwd': 'Qq654123',
        #                                  'governmentId': '330702197108020812'})
        # accounts = self.accountManager.getAccounts()
        self.ui.tWAccounts.signalCellContextMenu.connect(self.contextMenuEvent)
        
    def contextMenuEvent(self, event):
        print('account managerDLG')
