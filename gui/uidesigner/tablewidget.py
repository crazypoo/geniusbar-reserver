# -*- coding: utf-8 -*-
from PyQt4.QtGui import QTableWidget
from PyQt4.QtGui import QContextMenuEvent
from PyQt4.QtCore import pyqtSignal


class TableWidget(QTableWidget):
    sigCellContextMenu = pyqtSignal(QContextMenuEvent)

    def __init__(self, parent=None):
        super(TableWidget, self).__init__(parent)

    def contextMenuEvent(self, event):
        self.sigCellContextMenu.emit(event)
