# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitemplate/proxymanagedlg.ui'
#
# Created: Wed Dec 10 18:32:58 2014
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
        ProxyFinderDLG.resize(525, 291)
        self.layoutWidget = QtGui.QWidget(ProxyFinderDLG)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 0, 496, 267))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.retranslateUi(ProxyFinderDLG)
        QtCore.QMetaObject.connectSlotsByName(ProxyFinderDLG)

    def retranslateUi(self, ProxyFinderDLG):
        ProxyFinderDLG.setWindowTitle(_translate("ProxyFinderDLG", "代理管理", None))
        self.label.setText(_translate("ProxyFinderDLG", "地址：", None))
        self.pushButton.setText(_translate("ProxyFinderDLG", "更新", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ProxyFinderDLG", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ProxyFinderDLG", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ProxyFinderDLG", "新建行", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProxyFinderDLG", "地址", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProxyFinderDLG", "端口", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProxyFinderDLG", "掉包率", None))
        self.label_3.setText(_translate("ProxyFinderDLG", "端口：", None))
        self.label_2.setText(_translate("ProxyFinderDLG", "IP地址：", None))
        self.pushButton_2.setText(_translate("ProxyFinderDLG", "添加", None))
        self.pushButton_3.setText(_translate("ProxyFinderDLG", "取消", None))

