# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
import mainwindow
from widgetitem import WidgetItem


def main(proxyServers=None):
    app = QtGui.QApplication(sys.argv)
    main = mainwindow.MainWindow()
    main.show()
    app.exec_()
