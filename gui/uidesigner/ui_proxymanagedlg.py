# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitemplate/proxymanagedlg.ui'
#
# Created: Mon Dec 29 14:52:09 2014
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

class Ui_ProxyFinderDLG(object):
    def setupUi(self, ProxyFinderDLG):
        ProxyFinderDLG.setObjectName(_fromUtf8("ProxyFinderDLG"))
        ProxyFinderDLG.resize(489, 518)
        ProxyFinderDLG.setMaximumSize(QtCore.QSize(489, 16777215))
        self.verticalLayout_5 = QtGui.QVBoxLayout(ProxyFinderDLG)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(ProxyFinderDLG)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lEProxyUrl = QtGui.QLineEdit(self.groupBox_2)
        self.lEProxyUrl.setObjectName(_fromUtf8("lEProxyUrl"))
        self.horizontalLayout.addWidget(self.lEProxyUrl)
        self.pBUpdate = QtGui.QPushButton(self.groupBox_2)
        self.pBUpdate.setObjectName(_fromUtf8("pBUpdate"))
        self.horizontalLayout.addWidget(self.pBUpdate)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.progressBar = QtGui.QProgressBar(ProxyFinderDLG)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_5.addWidget(self.progressBar)
        self.groupBox = QtGui.QGroupBox(ProxyFinderDLG)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableWidget = TableWidget(self.groupBox)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(ProxyFinderDLG)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setMaximumSize(QtCore.QSize(43, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lEProxyIp = QtGui.QLineEdit(self.groupBox_4)
        self.lEProxyIp.setMaximumSize(QtCore.QSize(173, 20))
        self.lEProxyIp.setObjectName(_fromUtf8("lEProxyIp"))
        self.horizontalLayout_2.addWidget(self.lEProxyIp)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setMaximumSize(QtCore.QSize(33, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lEPort = QtGui.QLineEdit(self.groupBox_4)
        self.lEPort.setMaximumSize(QtCore.QSize(183, 20))
        self.lEPort.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lEPort.setObjectName(_fromUtf8("lEPort"))
        self.horizontalLayout_3.addWidget(self.lEPort)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pBAdd = QtGui.QPushButton(self.groupBox_4)
        self.pBAdd.setObjectName(_fromUtf8("pBAdd"))
        self.verticalLayout.addWidget(self.pBAdd)
        self.pBImport = QtGui.QPushButton(self.groupBox_4)
        self.pBImport.setObjectName(_fromUtf8("pBImport"))
        self.verticalLayout.addWidget(self.pBImport)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pBCancel = QtGui.QPushButton(ProxyFinderDLG)
        self.pBCancel.setObjectName(_fromUtf8("pBCancel"))
        self.horizontalLayout_5.addWidget(self.pBCancel)
        self.pBOk = QtGui.QPushButton(ProxyFinderDLG)
        self.pBOk.setObjectName(_fromUtf8("pBOk"))
        self.horizontalLayout_5.addWidget(self.pBOk)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.retranslateUi(ProxyFinderDLG)
        QtCore.QObject.connect(self.pBUpdate, QtCore.SIGNAL(_fromUtf8("clicked()")), ProxyFinderDLG.updateProxy)
        QtCore.QObject.connect(self.pBCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), ProxyFinderDLG.reject)
        QtCore.QObject.connect(self.pBAdd, QtCore.SIGNAL(_fromUtf8("clicked()")), ProxyFinderDLG.addProxy)
        QtCore.QObject.connect(self.pBImport, QtCore.SIGNAL(_fromUtf8("clicked()")), ProxyFinderDLG.importProxys)
        QtCore.QObject.connect(self.pBOk, QtCore.SIGNAL(_fromUtf8("clicked()")), ProxyFinderDLG.accept)
        QtCore.QMetaObject.connectSlotsByName(ProxyFinderDLG)

    def retranslateUi(self, ProxyFinderDLG):
        ProxyFinderDLG.setWindowTitle(_translate("ProxyFinderDLG", "代理管理", None))
        self.label.setText(_translate("ProxyFinderDLG", "地址：", None))
        self.pBUpdate.setText(_translate("ProxyFinderDLG", "更新", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ProxyFinderDLG", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ProxyFinderDLG", "新建行", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProxyFinderDLG", "地址", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProxyFinderDLG", "端口", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProxyFinderDLG", "掉包率", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProxyFinderDLG", "是否可用", None))
        self.label_2.setText(_translate("ProxyFinderDLG", "IP地址：", None))
        self.label_3.setText(_translate("ProxyFinderDLG", "端口：", None))
        self.pBAdd.setText(_translate("ProxyFinderDLG", "添加", None))
        self.pBImport.setText(_translate("ProxyFinderDLG", "导入", None))
        self.pBCancel.setText(_translate("ProxyFinderDLG", "取消", None))
        self.pBOk.setText(_translate("ProxyFinderDLG", "确定", None))

from tablewidget import TableWidget
