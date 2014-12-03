from PyQt4 import QtGui
from PyQt4 import QtCore
from uidesigner.ui_itemwidget import Ui_Item


class WidgetItem(QtGui.QWidget):
    def __init__(self, parent=None):
        super(WidgetItem, self).__init__(parent)
        self.ui = Ui_Item()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText('haha')
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        return
        self._starRating.paint(painter, self.rect(), self.palette(),
                StarRating.Editable)
    def render(self, painter, targetOffset=QtCore.QPoint(), sourceRegion=QtGui.QRegion(),
               flags=QtGui.QWidget.DrawWindowBackground|QtGui.QWidget.DrawChildren):
        self.ui.label.render(painter,targetOffset, sourceRegion, flags)
        self.ui.lineEdit.render(painter, targetOffset, sourceRegion, flags)
        
