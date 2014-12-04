# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uidesigner_res/accountdlg.ui'
#
# Created: Thu Dec 04 15:27:26 2014
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

class Ui_AccountDialog(object):
    def setupUi(self, AccountDialog):
        AccountDialog.setObjectName(_fromUtf8("AccountDialog"))
        AccountDialog.resize(243, 194)
        AccountDialog.setMaximumSize(QtCore.QSize(243, 194))
        self.verticalLayout_2 = QtGui.QVBoxLayout(AccountDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gBTaskinfo = QtGui.QGroupBox(AccountDialog)
        self.gBTaskinfo.setTitle(_fromUtf8(""))
        self.gBTaskinfo.setObjectName(_fromUtf8("gBTaskinfo"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gBTaskinfo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.gBTaskinfo)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lEAccount = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEAccount.setObjectName(_fromUtf8("lEAccount"))
        self.horizontalLayout.addWidget(self.lEAccount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.gBTaskinfo)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lEPasswd = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEPasswd.setEchoMode(QtGui.QLineEdit.Password)
        self.lEPasswd.setObjectName(_fromUtf8("lEPasswd"))
        self.horizontalLayout_2.addWidget(self.lEPasswd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.gBTaskinfo)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lEGovId = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEGovId.setObjectName(_fromUtf8("lEGovId"))
        self.horizontalLayout_3.addWidget(self.lEGovId)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.gBTaskinfo)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lEPhoneNumber = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEPhoneNumber.setObjectName(_fromUtf8("lEPhoneNumber"))
        self.horizontalLayout_4.addWidget(self.lEPhoneNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.gBTaskinfo)
        self.buttonBox = QtGui.QDialogButtonBox(AccountDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(AccountDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AccountDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AccountDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AccountDialog)

    def retranslateUi(self, AccountDialog):
        AccountDialog.setWindowTitle(_translate("AccountDialog", "账户添加", None))
        self.label.setText(_translate("AccountDialog", "账户ID:", None))
        self.label_2.setText(_translate("AccountDialog", "密码：", None))
        self.label_3.setText(_translate("AccountDialog", "身份证号：", None))
        self.label_4.setText(_translate("AccountDialog", "手机号：", None))

