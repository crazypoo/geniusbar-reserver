from PyQt4 import QtGui
from uidesigner.ui_viewerwidget import Ui_Widget


class WidgetItem(QtGui.QWidget):
    def __init__(self, id, parent=None):
        super(WidgetItem, self).__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.id = id
        self.ui.lEPhoneNumber = '123454_'+str(id)
