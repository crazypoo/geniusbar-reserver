# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitemplate/taskmanagedlg.ui'
#
# Created: Mon Dec 08 16:19:19 2014
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

class Ui_TaskManageDLG(object):
    def setupUi(self, TaskManageDLG):
        TaskManageDLG.setObjectName(_fromUtf8("TaskManageDLG"))
        TaskManageDLG.resize(650, 438)
        self.horizontalLayout_11 = QtGui.QHBoxLayout(TaskManageDLG)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(TaskManageDLG)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tWTasks = TaskTableWidget(self.groupBox)
        self.tWTasks.setObjectName(_fromUtf8("tWTasks"))
        self.tWTasks.setColumnCount(5)
        self.tWTasks.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tWTasks.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tWTasks.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tWTasks.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tWTasks.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tWTasks.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tWTasks)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(TaskManageDLG)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 171))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setMaximumSize(QtCore.QSize(44, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lETaskName = QtGui.QLineEdit(self.groupBox_4)
        self.lETaskName.setMaximumSize(QtCore.QSize(133, 20))
        self.lETaskName.setObjectName(_fromUtf8("lETaskName"))
        self.horizontalLayout.addWidget(self.lETaskName)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setMaximumSize(QtCore.QSize(89, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cBStoreName = QtGui.QComboBox(self.groupBox_4)
        self.cBStoreName.setObjectName(_fromUtf8("cBStoreName"))
        self.horizontalLayout_3.addWidget(self.cBStoreName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setMaximumSize(QtCore.QSize(89, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.cBReservType = QtGui.QComboBox(self.groupBox_4)
        self.cBReservType.setObjectName(_fromUtf8("cBReservType"))
        self.horizontalLayout_4.addWidget(self.cBReservType)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setMaximumSize(QtCore.QSize(33, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lEProxyIP = QtGui.QLineEdit(self.groupBox_4)
        self.lEProxyIP.setMaximumSize(QtCore.QSize(144, 20))
        self.lEProxyIP.setObjectName(_fromUtf8("lEProxyIP"))
        self.horizontalLayout_6.addWidget(self.lEProxyIP)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setMaximumSize(QtCore.QSize(33, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lEProxyPort = QtGui.QLineEdit(self.groupBox_4)
        self.lEProxyPort.setMaximumSize(QtCore.QSize(144, 20))
        self.lEProxyPort.setObjectName(_fromUtf8("lEProxyPort"))
        self.horizontalLayout_5.addWidget(self.lEProxyPort)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.pBAdd = QtGui.QPushButton(self.groupBox_4)
        self.pBAdd.setMaximumSize(QtCore.QSize(75, 23))
        self.pBAdd.setObjectName(_fromUtf8("pBAdd"))
        self.verticalLayout_4.addWidget(self.pBAdd)
        self.pBClear = QtGui.QPushButton(self.groupBox_4)
        self.pBClear.setMaximumSize(QtCore.QSize(75, 23))
        self.pBClear.setObjectName(_fromUtf8("pBClear"))
        self.verticalLayout_4.addWidget(self.pBClear)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_2 = QtGui.QGroupBox(TaskManageDLG)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lWAccounts = AccountListWidget(self.groupBox_2)
        self.lWAccounts.setMaximumSize(QtCore.QSize(237, 16777215))
        self.lWAccounts.setObjectName(_fromUtf8("lWAccounts"))
        item = QtGui.QListWidgetItem()
        self.lWAccounts.addItem(item)
        item = QtGui.QListWidgetItem()
        self.lWAccounts.addItem(item)
        self.verticalLayout_5.addWidget(self.lWAccounts)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(TaskManageDLG)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.pBOk = QtGui.QPushButton(self.groupBox_3)
        self.pBOk.setObjectName(_fromUtf8("pBOk"))
        self.horizontalLayout_7.addWidget(self.pBOk)
        self.pBCancel = QtGui.QPushButton(self.groupBox_3)
        self.pBCancel.setObjectName(_fromUtf8("pBCancel"))
        self.horizontalLayout_7.addWidget(self.pBCancel)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.retranslateUi(TaskManageDLG)
        QtCore.QObject.connect(self.pBAdd, QtCore.SIGNAL(_fromUtf8("clicked()")), TaskManageDLG.addTask)
        QtCore.QObject.connect(self.tWTasks, QtCore.SIGNAL(_fromUtf8("cellClicked(int,int)")), TaskManageDLG.taskCellClicked)
        QtCore.QObject.connect(self.pBCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), TaskManageDLG.reject)
        QtCore.QObject.connect(self.pBOk, QtCore.SIGNAL(_fromUtf8("clicked()")), TaskManageDLG.accept)
        QtCore.QMetaObject.connectSlotsByName(TaskManageDLG)

    def retranslateUi(self, TaskManageDLG):
        TaskManageDLG.setWindowTitle(_translate("TaskManageDLG", "任务管理", None))
        self.groupBox.setTitle(_translate("TaskManageDLG", "任务列表", None))
        item = self.tWTasks.horizontalHeaderItem(0)
        item.setText(_translate("TaskManageDLG", "任务名", None))
        item = self.tWTasks.horizontalHeaderItem(1)
        item.setText(_translate("TaskManageDLG", "零售商店", None))
        item = self.tWTasks.horizontalHeaderItem(2)
        item.setText(_translate("TaskManageDLG", "服务类型", None))
        item = self.tWTasks.horizontalHeaderItem(3)
        item.setText(_translate("TaskManageDLG", "代理", None))
        item = self.tWTasks.horizontalHeaderItem(4)
        item.setText(_translate("TaskManageDLG", "端口", None))
        self.groupBox_4.setTitle(_translate("TaskManageDLG", "添加任务列表", None))
        self.label.setText(_translate("TaskManageDLG", "任务名：", None))
        self.label_2.setText(_translate("TaskManageDLG", "零售店：", None))
        self.label_3.setText(_translate("TaskManageDLG", "服务类型：", None))
        self.label_4.setText(_translate("TaskManageDLG", "代理：", None))
        self.label_5.setText(_translate("TaskManageDLG", "端口：", None))
        self.pBAdd.setText(_translate("TaskManageDLG", "添加", None))
        self.pBClear.setText(_translate("TaskManageDLG", "清空", None))
        self.groupBox_2.setTitle(_translate("TaskManageDLG", "列表成员", None))
        __sortingEnabled = self.lWAccounts.isSortingEnabled()
        self.lWAccounts.setSortingEnabled(False)
        item = self.lWAccounts.item(0)
        item.setText(_translate("TaskManageDLG", "账号1", None))
        item = self.lWAccounts.item(1)
        item.setText(_translate("TaskManageDLG", "账号2", None))
        self.lWAccounts.setSortingEnabled(__sortingEnabled)
        self.pBOk.setText(_translate("TaskManageDLG", "确定", None))
        self.pBCancel.setText(_translate("TaskManageDLG", "取消", None))

from tasktablewidget import TaskTableWidget
from accountlistwidget import AccountListWidget
