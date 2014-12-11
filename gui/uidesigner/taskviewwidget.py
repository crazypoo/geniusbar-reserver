from PyQt4.QtGui import QWidget, QTableWidgetItem
from gui.uidesigner.ui_taskviewwidget import Ui_Form
from PyQt4.QtCore import pyqtSignal, QString


class TaskViewWidget(QWidget):
    sigRefresh = pyqtSignal()
    sigSubmit = pyqtSignal()
    sigTimeSlot = pyqtSignal(str)

    def __init__(self, parent=None):
        super(TaskViewWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.contents = {}
        self.selectedtime = None

    def refresh(self):
        self.sigRefresh.emit()

    def submit(self):
        self.sigSubmit.emit()

    def __getattr__(self, name):
        return getattr(self.ui, name)

    def fillTableWidget(self, data, rowmax):
        self.ui.tableWidget.setColumnCount(len(data))
        self.ui.tableWidget.setRowCount(rowmax)
        index = 0
        for item in data:
            for name, times in item.items():
                item = QTableWidgetItem()
                item.setText(QString(name))
                self.ui.tableWidget.setHorizontalHeaderItem(index, item)
                i = 0
                for time, id in times:
                    item = QTableWidgetItem()
                    item.setText(QString(time))
                    self.ui.tableWidget.setItem(i, index, item)
                    self.contents['%s%s' % (i, index)] = id
                    i += 1
            index += 1

    def cellClicked(self, row, col):
        # print('cellClicked %s %s' % (row, col))
        key = '%s%s' % (row, col)
        self.selectedtime = self.contents[key]

    def cellDoubleClicked(self, row, col):
        # print('cellDoubleClicked %s %s' % (row, col))
        try:
            key = '%s%s' % (row, col)
            self.selectedtime = self.contents[key]
            self.sigTimeSlot.emit(self.contents[key])
            self.ui.stackedWidget.setCurrentIndex(0)
        except:
            self.sigTimeSlot.emit('testclicked')

    def accept(self):
        if self.selectedtime:
            self.sigTimeSlot.emit(self.selectedtime)
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.sigTimeSlot.emit('testclicked')


    def rejected(self):
        self.ui.stackedWidget.setCurrentIndex(0)
