# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitemplate/taskview.ui'
#
# Created: Tue Dec 09 15:47:56 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(473, 329)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_11 = QtGui.QGroupBox(Form)
        self.groupBox_11.setTitle(_fromUtf8(""))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_11)
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_6)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progressBar.setProperty("value", 1)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_11.addWidget(self.progressBar)
        self.verticalLayout_4.addWidget(self.groupBox_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.groupBox_12 = QtGui.QGroupBox(self.groupBox_11)
        self.groupBox_12.setSizeIncrement(QtCore.QSize(5, 5))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.groupBox_12)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.pTSmsChallengeTip = QtGui.QPlainTextEdit(self.groupBox_12)
        self.pTSmsChallengeTip.setMinimumSize(QtCore.QSize(180, 90))
        self.pTSmsChallengeTip.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pTSmsChallengeTip.setObjectName(_fromUtf8("pTSmsChallengeTip"))
        self.verticalLayout_14.addWidget(self.pTSmsChallengeTip)
        self.groupBox_13 = QtGui.QGroupBox(self.groupBox_12)
        self.groupBox_13.setMaximumSize(QtCore.QSize(200, 70))
        self.groupBox_13.setTitle(_fromUtf8(""))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.groupBox_13)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.groupBox_13)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lEPhoneNumber = QtGui.QLineEdit(self.groupBox_13)
        self.lEPhoneNumber.setEnabled(True)
        self.lEPhoneNumber.setObjectName(_fromUtf8("lEPhoneNumber"))
        self.horizontalLayout_8.addWidget(self.lEPhoneNumber)
        self.verticalLayout_15.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_7 = QtGui.QLabel(self.groupBox_13)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lESmsCode = QtGui.QLineEdit(self.groupBox_13)
        self.lESmsCode.setEnabled(True)
        self.lESmsCode.setMaximumSize(QtCore.QSize(128, 20))
        self.lESmsCode.setObjectName(_fromUtf8("lESmsCode"))
        self.horizontalLayout_9.addWidget(self.lESmsCode)
        self.verticalLayout_15.addLayout(self.horizontalLayout_9)
        self.verticalLayout_14.addWidget(self.groupBox_13)
        self.horizontalLayout_5.addWidget(self.groupBox_12)
        self.groupBox_14 = QtGui.QGroupBox(self.groupBox_11)
        self.groupBox_14.setTitle(_fromUtf8(""))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.groupBox_14)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.groupBox_15 = QtGui.QGroupBox(self.groupBox_14)
        self.groupBox_15.setMinimumSize(QtCore.QSize(170, 80))
        self.groupBox_15.setTitle(_fromUtf8(""))
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbVerifyCodePic = QtGui.QLabel(self.groupBox_15)
        self.lbVerifyCodePic.setMaximumSize(QtCore.QSize(161, 78))
        self.lbVerifyCodePic.setObjectName(_fromUtf8("lbVerifyCodePic"))
        self.horizontalLayout_4.addWidget(self.lbVerifyCodePic)
        self.verticalLayout_16.addWidget(self.groupBox_15)
        self.groupBox_16 = QtGui.QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_16)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lECaptchaAnswer = QtGui.QLineEdit(self.groupBox_16)
        self.lECaptchaAnswer.setObjectName(_fromUtf8("lECaptchaAnswer"))
        self.verticalLayout_3.addWidget(self.lECaptchaAnswer)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pBRefresh = QtGui.QPushButton(self.groupBox_16)
        self.pBRefresh.setObjectName(_fromUtf8("pBRefresh"))
        self.horizontalLayout_3.addWidget(self.pBRefresh)
        self.pBSumit = QtGui.QPushButton(self.groupBox_16)
        self.pBSumit.setMaximumSize(QtCore.QSize(75, 23))
        self.pBSumit.setObjectName(_fromUtf8("pBSumit"))
        self.horizontalLayout_3.addWidget(self.pBSumit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_16.addWidget(self.groupBox_16)
        self.horizontalLayout_5.addWidget(self.groupBox_14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_12.setTitle(_translate("Form", "发送预约码", None))
        self.label_6.setText(_translate("Form", "手机号：", None))
        self.label_7.setText(_translate("Form", "预约码：", None))
        self.lbVerifyCodePic.setText(_translate("Form", "TextLabel", None))
        self.groupBox_16.setTitle(_translate("Form", "输入验证码", None))
        self.pBRefresh.setText(_translate("Form", "刷新", None))
        self.pBSumit.setText(_translate("Form", "确定", None))

