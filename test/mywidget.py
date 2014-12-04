# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
import sys

class MyListModel(QAbstractListModel):
    def __init__(self,parent=None):
        super(MyListModel,self).__init__(parent)
        self._data=[70,90,20,50]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self,index,role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        row=index.row()
        if role==Qt.DisplayRole:
            return self._data[row]
        return QVariant()

class MyDelegate(QStyledItemDelegate):
    def paint(self,painter,option,index):

        item_var = index.data(Qt.DisplayRole)
        item_str = item_var.toPyObject()

        opts = QStyleOptionProgressBarV2()
        opts.rect = option.rect
        opts.minimum = 0
        opts.maximum = 100
        opts.text = str(item_str)
        opts.textAlignment = Qt.AlignCenter
        opts.textVisible = True
        opts.progress = int(item_str)
        QApplication.style().drawControl(QStyle.CE_ProgressBar, opts, painter)

def main(): 
    app=QApplication(sys.argv)
    model=MyListModel()
    delegate=MyDelegate()
    view=QListView()
    view.setModel(model)
    view.setItemDelegate(delegate)
    view.show()
    sys.exit(app.exec_())

main()
