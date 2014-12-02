# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtaskdlg.ui'
#
# Created: Tue Dec 02 15:49:21 2014
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

class Ui_NewTaskDialog(object):
    def setupUi(self, NewTaskDialog):
        NewTaskDialog.setObjectName(_fromUtf8("NewTaskDialog"))
        NewTaskDialog.resize(295, 258)
        self.gBTaskinfo = QtGui.QGroupBox(NewTaskDialog)
        self.gBTaskinfo.setGeometry(QtCore.QRect(20, 10, 259, 241))
        self.gBTaskinfo.setTitle(_fromUtf8(""))
        self.gBTaskinfo.setObjectName(_fromUtf8("gBTaskinfo"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gBTaskinfo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lebelStore = QtGui.QLabel(self.gBTaskinfo)
        self.lebelStore.setMaximumSize(QtCore.QSize(116, 16777215))
        self.lebelStore.setObjectName(_fromUtf8("lebelStore"))
        self.horizontalLayout.addWidget(self.lebelStore)
        self.combStore = QtGui.QComboBox(self.gBTaskinfo)
        self.combStore.setMinimumSize(QtCore.QSize(115, 0))
        self.combStore.setObjectName(_fromUtf8("combStore"))
        self.horizontalLayout.addWidget(self.combStore)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_7 = QtGui.QLabel(self.gBTaskinfo)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.combServType = QtGui.QComboBox(self.gBTaskinfo)
        self.combServType.setMinimumSize(QtCore.QSize(115, 0))
        self.combServType.setObjectName(_fromUtf8("combServType"))
        self.horizontalLayout_2.addWidget(self.combServType)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.gBTaskinfo)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.lEUserName = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEUserName.setObjectName(_fromUtf8("lEUserName"))
        self.horizontalLayout_3.addWidget(self.lEUserName)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.gBTaskinfo)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lEPasswd = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEPasswd.setEchoMode(QtGui.QLineEdit.Password)
        self.lEPasswd.setObjectName(_fromUtf8("lEPasswd"))
        self.horizontalLayout_4.addWidget(self.lEPasswd)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.gBTaskinfo)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lEGovId = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEGovId.setObjectName(_fromUtf8("lEGovId"))
        self.horizontalLayout_5.addWidget(self.lEGovId)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.gBTaskinfo)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lEPhoneNumber = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEPhoneNumber.setObjectName(_fromUtf8("lEPhoneNumber"))
        self.horizontalLayout_6.addWidget(self.lEPhoneNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_5 = QtGui.QLabel(self.gBTaskinfo)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lEReservCode = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEReservCode.setObjectName(_fromUtf8("lEReservCode"))
        self.horizontalLayout_7.addWidget(self.lEReservCode)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pBOk = QtGui.QPushButton(self.gBTaskinfo)
        self.pBOk.setEnabled(True)
        self.pBOk.setObjectName(_fromUtf8("pBOk"))
        self.horizontalLayout_8.addWidget(self.pBOk)
        self.pBImport = QtGui.QPushButton(self.gBTaskinfo)
        self.pBImport.setObjectName(_fromUtf8("pBImport"))
        self.horizontalLayout_8.addWidget(self.pBImport)
        self.pBClear = QtGui.QPushButton(self.gBTaskinfo)
        self.pBClear.setObjectName(_fromUtf8("pBClear"))
        self.horizontalLayout_8.addWidget(self.pBClear)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(NewTaskDialog)
        QtCore.QObject.connect(self.pBOk, QtCore.SIGNAL(_fromUtf8("clicked()")), NewTaskDialog.startTask)
        QtCore.QObject.connect(self.pBImport, QtCore.SIGNAL(_fromUtf8("clicked()")), NewTaskDialog.importUser)
        QtCore.QMetaObject.connectSlotsByName(NewTaskDialog)

    def retranslateUi(self, NewTaskDialog):
        NewTaskDialog.setWindowTitle(_translate("NewTaskDialog", "新建任务", None))
        self.lebelStore.setText(_translate("NewTaskDialog", "零售店：", None))
        self.label_7.setText(_translate("NewTaskDialog", "服务类型:", None))
        self.label.setText(_translate("NewTaskDialog", "用户名：", None))
        self.label_2.setText(_translate("NewTaskDialog", "密码：", None))
        self.label_3.setText(_translate("NewTaskDialog", "身份证号：", None))
        self.label_4.setText(_translate("NewTaskDialog", "手机号：", None))
        self.label_5.setText(_translate("NewTaskDialog", "预约码：", None))
        self.pBOk.setText(_translate("NewTaskDialog", "确认", None))
        self.pBImport.setText(_translate("NewTaskDialog", "导入", None))
        self.pBClear.setText(_translate("NewTaskDialog", "清空", None))

