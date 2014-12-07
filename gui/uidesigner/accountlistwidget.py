# -*- coding: utf-8 -*-
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QContextMenuEvent
from PyQt4.QtCore import pyqtSignal


class AccountListWidget(QListWidget):
    signalCellContextMenu = pyqtSignal(QContextMenuEvent)

    def __init__(self, parent=None):
        super(AccountListWidget, self).__init__(parent)

    def contextMenuEvent(self, event):
        self.signalCellContextMenu.emit(event)