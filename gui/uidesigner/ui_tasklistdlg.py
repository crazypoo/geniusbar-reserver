# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitemplate/tasklistdlg.ui'
#
# Created: Sat Dec 13 11:46:11 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TaskListDLG(object):
    def setupUi(self, TaskListDLG):
        TaskListDLG.setObjectName(_fromUtf8("TaskListDLG"))
        TaskListDLG.resize(279, 312)
        self.verticalLayout_2 = QtGui.QVBoxLayout(TaskListDLG)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(TaskListDLG)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = AccountListWidget(self.groupBox)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(TaskListDLG)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(TaskListDLG)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TaskListDLG.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TaskListDLG.reject)
        QtCore.QMetaObject.connectSlotsByName(TaskListDLG)

    def retranslateUi(self, TaskListDLG):
        TaskListDLG.setWindowTitle(_translate("TaskListDLG", "任务列表", None))

from accountlistwidget import AccountListWidget
