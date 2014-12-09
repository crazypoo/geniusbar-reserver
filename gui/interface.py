# -*- coding: utf-8 -*-
import sys
import os
from PyQt4 import QtGui
from mainwindowq import MainWindow


def main(proxyServers=None):
    app = QtGui.QApplication(sys.argv)
    main = MainWindow(os.path.abspath(os.getcwd()))
    main.show()
    app.exec_()
