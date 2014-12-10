from PyQt4.QtGui import QWidget
from uidesigner.ui_taskviewwidget import Ui_Form
from PyQt4.QtCore import pyqtSignal


class TaskViewWidget(QWidget):
    sigRefresh = pyqtSignal()
    sigSubmit = pyqtSignal()

    def __init__(self, parent=None):
        super(TaskViewWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def refresh(self):
        self.sigRefresh.emit()

    def submit(self):
        self.sigSubmit.emit()

    def __getattr__(self, name):
        return getattr(self.ui, name)
