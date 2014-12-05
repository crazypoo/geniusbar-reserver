# -*- coding: utf-8 -*-
from PyQt4.QtGui import QTableWidget
from PyQt4.QtGui import QContextMenuEvent
from PyQt4.QtCore import pyqtSignal


class TaskTableWidget(QTableWidget):
    signalCellContextMenu = pyqtSignal(QContextMenuEvent)

    def __init__(self, parent=None):
        super(TaskTableWidget, self).__init__(parent)

    def contextMenuEvent(self, event):
        self.signalCellContextMenu.emit(event)
