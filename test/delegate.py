import sys
sys.path.append('..')
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.QtGui as QtGui
from gui.itemwidget import WidgetItem


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())


class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        # create objects
        items = [WidgetItem()]
        lm = MyListModel(items, self)
        de = MyDelegate(self)
        lv = QListView()
        lv.setModel(lm)
        lv.setItemDelegate(de)
        # layout
        layout = QVBoxLayout()
        layout.addWidget(lv)
        self.setLayout(layout)


class MyDelegate(QtGui.QStyledItemDelegate):
    def __init__(self, parent=None, *args):
        QtGui.QStyledItemDelegate.__init__(self, parent, *args)

    def createEditor(self, parent, option, index):
        print('createEditorData %s' % index.row())
        return WidgetItem(parent)

    def setEditorData(self, editor, index):
        print(type(editor))

    def setModelData(self, editor, model, index):
        print(type(model))

    def paint(self, painter, option, index):
        painter.save()
        data = index.data()
        widgetItem = data.toPyObject()
        print(type(widgetItem))
        # set background color
        painter.setPen(QPen(Qt.NoPen))
        if option.state & QStyle.State_Selected:
            painter.setBrush(QBrush(Qt.red))
        else:
            painter.setBrush(QBrush(Qt.white))
        print(widgetItem.ui.lineEdit.rect())
        print(option.rect)
        if isinstance(widgetItem, WidgetItem):
            widgetItem.render(painter)
        else:
            super(MyDelegate, self).paint(painter, option, index)
       # .QStyle().drawControl(QStyle.CT_LineEdit, option, painter, QtGui.QLineEdit())
        #drawControl(QStyle.CE_ItemViewItem, item, painter)
        painter.restore()

####################################################################  
class MyListModel(QAbstractListModel):  
    def __init__(self, datain, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractTableModel.__init__(self, parent, *args)
        self.listdata = datain
  
    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)
  
    def data(self, index, role):
       # print('data %s' % index.row())
        if index.isValid() and role == Qt.DisplayRole:
            #print(type(self.listdata[index.row()]))
            return QVariant(self.listdata[index.row()])
        else:
            return QVariant()
####################################################################  
if __name__ == "__main__":  
    main()  
