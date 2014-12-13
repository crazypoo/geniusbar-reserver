# -*- coding: utf-8 -*-
from PyQt4.QtGui import QWidget, QTableWidgetItem
from PyQt4.QtCore import QString
from uidesigner import ui_tablewidget
#from PyQt4.QtCore import pyqtSignal


class TableWidget(QWidget):

    def __init__(self, headers=None, parent=None):
        super(TableWidget, self).__init__(parent)
        self.ui = ui_tablewidget.Ui_Form()
        self.ui.setupUi(self)
        self.setupHeaders(headers)
        horheader = self.ui.tableWidget.horizontalHeader()
        horheader.setStretchLastSection(True)

    def setupHeaders(self, headers):
        if not headers:
            return
        self.setColumnCount(len(headers))
        for col, header in enumerate(headers):
            item = QTableWidgetItem()
            item.setText(QString(header))
            self.setHorizontalHeaderItem(col, item)

    def __getattr__(self, name):
        try:
            return getattr(self.ui.tableWidget, name)
        except:
            pass

    #def contextMenuEvent(self, event):
    #print('contextMenuEvent')
        # actfun = partial(self._removeAccout, str(item.text()))
        # self.act_delete = QAction(u'删除', self, triggered=actfun)

        # popMenu = QMenu()
        # popMenu.addAction(self.act_delete)
        # popMenu.exec_(self.cursor().pos())
