# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from multiprocessing import freeze_support
import mainwindow
from widgetitem import WidgetItem


def main():
    freeze_support()
    app = QtGui.QApplication(sys.argv)
    main = WidgetItem()#mainwindow.MainWindow()
    main.show()
    app.exec_()
