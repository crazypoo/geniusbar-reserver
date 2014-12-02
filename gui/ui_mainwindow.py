# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(714, 556)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        self.menu_task_manage = QtGui.QMenu(self.menubar)
        self.menu_task_manage.setObjectName(_fromUtf8("menu_task_manage"))
        self.menu_account_manage = QtGui.QMenu(self.menubar)
        self.menu_account_manage.setObjectName(_fromUtf8("menu_account_manage"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName(_fromUtf8("action_5"))
        self.action_new_task = QtGui.QAction(MainWindow)
        self.action_new_task.setObjectName(_fromUtf8("action_new_task"))
        self.action_10 = QtGui.QAction(MainWindow)
        self.action_10.setObjectName(_fromUtf8("action_10"))
        self.action_11 = QtGui.QAction(MainWindow)
        self.action_11.setObjectName(_fromUtf8("action_11"))
        self.action_new_task_2 = QtGui.QAction(MainWindow)
        self.action_new_task_2.setObjectName(_fromUtf8("action_new_task_2"))
        self.action_view_task = QtGui.QAction(MainWindow)
        self.action_view_task.setObjectName(_fromUtf8("action_view_task"))
        self.action_create_task = QtGui.QAction(MainWindow)
        self.action_create_task.setObjectName(_fromUtf8("action_create_task"))
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName(_fromUtf8("action_6"))
        self.action_7 = QtGui.QAction(MainWindow)
        self.action_7.setObjectName(_fromUtf8("action_7"))
        self.action_8 = QtGui.QAction(MainWindow)
        self.action_8.setObjectName(_fromUtf8("action_8"))
        self.action_add_account = QtGui.QAction(MainWindow)
        self.action_add_account.setObjectName(_fromUtf8("action_add_account"))
        self.action_13 = QtGui.QAction(MainWindow)
        self.action_13.setObjectName(_fromUtf8("action_13"))
        self.action_14 = QtGui.QAction(MainWindow)
        self.action_14.setObjectName(_fromUtf8("action_14"))
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu_2.addAction(self.action_4)
        self.menu_2.addSeparator()
        self.menu_3.addAction(self.action_11)
        self.menu_task_manage.addAction(self.action_create_task)
        self.menu_task_manage.addAction(self.action_view_task)
        self.menu_account_manage.addAction(self.action_add_account)
        self.menu_account_manage.addAction(self.action_13)
        self.menu_account_manage.addAction(self.action_14)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_task_manage.menuAction())
        self.menubar.addAction(self.menu_account_manage.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_create_task, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.newTask)
        QtCore.QObject.connect(self.action_add_account, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.addAccount)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_2.setTitle(_translate("MainWindow", "编辑", None))
        self.menu_3.setTitle(_translate("MainWindow", "帮助", None))
        self.menu_task_manage.setTitle(_translate("MainWindow", "任务管理", None))
        self.menu_account_manage.setTitle(_translate("MainWindow", "用户管理", None))
        self.action.setText(_translate("MainWindow", "登录", None))
        self.action_2.setText(_translate("MainWindow", "注销", None))
        self.action_4.setText(_translate("MainWindow", "任务配置", None))
        self.action_5.setText(_translate("MainWindow", "新建任务", None))
        self.action_new_task.setText(_translate("MainWindow", "新建任务", None))
        self.action_10.setText(_translate("MainWindow", "查看", None))
        self.action_11.setText(_translate("MainWindow", "关于", None))
        self.action_new_task_2.setText(_translate("MainWindow", "新建任务", None))
        self.action_view_task.setText(_translate("MainWindow", "查看", None))
        self.action_create_task.setText(_translate("MainWindow", "新建任务", None))
        self.action_6.setText(_translate("MainWindow", "添加用户", None))
        self.action_7.setText(_translate("MainWindow", "删除用户", None))
        self.action_8.setText(_translate("MainWindow", "修改", None))
        self.action_add_account.setText(_translate("MainWindow", "添加账号", None))
        self.action_13.setText(_translate("MainWindow", "删除账号", None))
        self.action_14.setText(_translate("MainWindow", "修改账号", None))

