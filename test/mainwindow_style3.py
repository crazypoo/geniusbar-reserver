import sys
sys.path.append('..')
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from gui.widgetitem import WidgetItem


class MainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.item1 = WidgetItem(1)
        self.item2 = WidgetItem(2)
        self.stackedWidget = QtGui.QStackedWidget()
        self.stackedWidget.addWidget(self.item1)
        self.stackedWidget.addWidget(self.item2)
        self.stackedWidget.setCurrentIndex(1)
        self.pushbutton = QtGui.QPushButton()
        self.mainlayout = QtGui.QHBoxLayout(self)
        self.mainlayout.addWidget(self.stackedWidget)
        self.mainlayout.addWidget(self.pushbutton)
        self.pushbutton.clicked.connect(self.onOk)


    def onOk(self):
        index = self.stackedWidget.currentIndex()
        if index == 0:
            self.stackedWidget.setCurrentIndex(1)
            self.stackedWidget.widget(1).ui.lEVerfiyCode.setText('134')
        else:
            self.stackedWidget.setCurrentIndex(0)


def main():
    app = QtGui.QApplication(sys.argv)
    spliterH = QtGui.QSplitter(QtCore.Qt.Horizontal, 0)
    item = WidgetItem(spliterH)

    spliterV = QtGui.QSplitter(QtCore.Qt.Vertical, spliterH)
    item2 = WidgetItem(spliterV)

    spliter = QtGui.QSplitter(QtCore.Qt.Vertical, spliterV)
    item3 = WidgetItem(spliter)
    spliterH.setStretchFactor(1,1)
    spliterH.show()

    app.exec_()

main()
