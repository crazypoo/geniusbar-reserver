# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from PyQt4.QtGui import QDialog, QApplication, QListWidgetItem

from gui.uidesigner.ui_accountlistdlg import Ui_AccountListDLG


class TestListWidget(QDialog):
    def __init__(self, parent=None):
        super(TestListWidget, self).__init__(parent)
        self.ui = Ui_AccountListDLG()
        self.ui.setupUi(self)

    def accept(self):
        print(self.ui.listWidget.selectedItems())

def main(proxyServers=None):
    app = QApplication(sys.argv)
    main = TestListWidget()
    for i in range(10):
        item = QListWidgetItem()
        item.setText('%s' % i)
        main.ui.listWidget.addItem(item)

    main.ui.listWidget.setSelectionMode(2)
    main.show()
    app.exec_()


if __name__=='__main__':
    main()
