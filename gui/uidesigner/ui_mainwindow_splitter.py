# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitemplate/mainwindow_splitter.ui'
#
# Created: Fri Dec 26 14:09:48 2014
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
        MainWindow.resize(1000, 653)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        self.menu_4 = QtGui.QMenu(self.menubar)
        self.menu_4.setObjectName(_fromUtf8("menu_4"))
        self.menu_5 = QtGui.QMenu(self.menubar)
        self.menu_5.setObjectName(_fromUtf8("menu_5"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBarMgr = QtGui.QToolBar(MainWindow)
        self.toolBarMgr.setObjectName(_fromUtf8("toolBarMgr"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarMgr)
        self.toolBarApp = QtGui.QToolBar(MainWindow)
        self.toolBarApp.setObjectName(_fromUtf8("toolBarApp"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarApp)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_start_task = QtGui.QAction(MainWindow)
        self.action_start_task.setEnabled(True)
        self.action_start_task.setObjectName(_fromUtf8("action_start_task"))
        self.action_import_task = QtGui.QAction(MainWindow)
        self.action_import_task.setObjectName(_fromUtf8("action_import_task"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_accountmanage = QtGui.QAction(MainWindow)
        self.action_accountmanage.setObjectName(_fromUtf8("action_accountmanage"))
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName(_fromUtf8("action_6"))
        self.action_7 = QtGui.QAction(MainWindow)
        self.action_7.setObjectName(_fromUtf8("action_7"))
        self.action_9 = QtGui.QAction(MainWindow)
        self.action_9.setObjectName(_fromUtf8("action_9"))
        self.action_10 = QtGui.QAction(MainWindow)
        self.action_10.setObjectName(_fromUtf8("action_10"))
        self.action_task_manage = QtGui.QAction(MainWindow)
        self.action_task_manage.setObjectName(_fromUtf8("action_task_manage"))
        self.action_8 = QtGui.QAction(MainWindow)
        self.action_8.setObjectName(_fromUtf8("action_8"))
        self.action_proxy_manager = QtGui.QAction(MainWindow)
        self.action_proxy_manager.setObjectName(_fromUtf8("action_proxy_manager"))
        self.action_12 = QtGui.QAction(MainWindow)
        self.action_12.setObjectName(_fromUtf8("action_12"))
        self.action_stop_task = QtGui.QAction(MainWindow)
        self.action_stop_task.setObjectName(_fromUtf8("action_stop_task"))
        self.action_view_detail = QtGui.QAction(MainWindow)
        self.action_view_detail.setObjectName(_fromUtf8("action_view_detail"))
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_7)
        self.menu_2.addAction(self.action_start_task)
        self.menu_2.addAction(self.action_import_task)
        self.menu_2.addAction(self.action_stop_task)
        self.menu_2.addAction(self.action_view_detail)
        self.menu_3.addAction(self.action_4)
        self.menu_4.addAction(self.action_task_manage)
        self.menu_4.addAction(self.action_accountmanage)
        self.menu_4.addAction(self.action_proxy_manager)
        self.menu_5.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_task_manage, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.taskManage)
        QtCore.QObject.connect(self.action_accountmanage, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.accountManage)
        QtCore.QObject.connect(self.action_start_task, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.startTask)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("destroyed()")), MainWindow.close)
        QtCore.QObject.connect(self.action_import_task, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.importTask)
        QtCore.QObject.connect(self.action_view_detail, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.viewDetail)
        QtCore.QObject.connect(self.action_proxy_manager, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.proxyMgr)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "天才吧预约", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_2.setTitle(_translate("MainWindow", "任务", None))
        self.menu_3.setTitle(_translate("MainWindow", "设置", None))
        self.menu_4.setTitle(_translate("MainWindow", "管理", None))
        self.menu_5.setTitle(_translate("MainWindow", "帮助", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBarMgr.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.toolBarApp.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.action.setText(_translate("MainWindow", "配置", None))
        self.action_start_task.setText(_translate("MainWindow", "开始任务", None))
        self.action_import_task.setText(_translate("MainWindow", "导入任务", None))
        self.action_4.setText(_translate("MainWindow", "任务列表", None))
        self.action_accountmanage.setText(_translate("MainWindow", "账号管理", None))
        self.action_6.setText(_translate("MainWindow", "关于", None))
        self.action_7.setText(_translate("MainWindow", "登录", None))
        self.action_9.setText(_translate("MainWindow", "更新代理列表", None))
        self.action_10.setText(_translate("MainWindow", "自定义代理", None))
        self.action_task_manage.setText(_translate("MainWindow", "任务管理", None))
        self.action_8.setText(_translate("MainWindow", "计划任务", None))
        self.action_proxy_manager.setText(_translate("MainWindow", "代理管理", None))
        self.action_12.setText(_translate("MainWindow", "账号管理", None))
        self.action_stop_task.setText(_translate("MainWindow", "停止任务", None))
        self.action_view_detail.setText(_translate("MainWindow", "查看", None))

