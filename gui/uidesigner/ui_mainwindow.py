# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitemplate/mainwindow.ui'
#
# Created: Fri Dec 05 18:25:25 2014
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
        MainWindow.resize(956, 630)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gBListName = QtGui.QGroupBox(self.tab)
        self.gBListName.setObjectName(_fromUtf8("gBListName"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.gBListName)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tWTaskList = QtGui.QTableWidget(self.gBListName)
        self.tWTaskList.setObjectName(_fromUtf8("tWTaskList"))
        self.tWTaskList.setColumnCount(5)
        self.tWTaskList.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tWTaskList.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tWTaskList.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tWTaskList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tWTaskList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tWTaskList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tWTaskList.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tWTaskList.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_2.addWidget(self.tWTaskList)
        self.verticalLayout_2.addWidget(self.gBListName)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_current = QtGui.QWidget()
        self.tab_current.setObjectName(_fromUtf8("tab_current"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_current)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gBTaskName = QtGui.QGroupBox(self.tab_current)
        self.gBTaskName.setObjectName(_fromUtf8("gBTaskName"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.gBTaskName)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.tWComplete = QtGui.QTableWidget(self.gBTaskName)
        self.tWComplete.setObjectName(_fromUtf8("tWComplete"))
        self.tWComplete.setColumnCount(4)
        self.tWComplete.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tWComplete.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tWComplete.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tWComplete.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tWComplete.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tWComplete.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tWComplete.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_7.addWidget(self.tWComplete)
        self.verticalLayout_6.addWidget(self.gBTaskName)
        self.tabWidget.addTab(self.tab_current, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.groupBox_2)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_11 = QtGui.QGroupBox(self.page)
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
        self.lEReservCode = QtGui.QLineEdit(self.groupBox_13)
        self.lEReservCode.setEnabled(True)
        self.lEReservCode.setMaximumSize(QtCore.QSize(128, 20))
        self.lEReservCode.setObjectName(_fromUtf8("lEReservCode"))
        self.horizontalLayout_9.addWidget(self.lEReservCode)
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
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_16)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lEVerfiyCode = QtGui.QLineEdit(self.groupBox_16)
        self.lEVerfiyCode.setObjectName(_fromUtf8("lEVerfiyCode"))
        self.horizontalLayout_3.addWidget(self.lEVerfiyCode)
        self.pBOk_2 = QtGui.QPushButton(self.groupBox_16)
        self.pBOk_2.setMaximumSize(QtCore.QSize(75, 23))
        self.pBOk_2.setObjectName(_fromUtf8("pBOk_2"))
        self.horizontalLayout_3.addWidget(self.pBOk_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_16.addWidget(self.groupBox_16)
        self.horizontalLayout_5.addWidget(self.groupBox_14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.groupBox_11)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 21))
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
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
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
        self.action_11 = QtGui.QAction(MainWindow)
        self.action_11.setObjectName(_fromUtf8("action_11"))
        self.action_12 = QtGui.QAction(MainWindow)
        self.action_12.setObjectName(_fromUtf8("action_12"))
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_7)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_3.addAction(self.action_4)
        self.menu_4.addAction(self.action_task_manage)
        self.menu_4.addAction(self.action_accountmanage)
        self.menu_4.addAction(self.action_11)
        self.menu_5.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.action_task_manage, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.taskManage)
        QtCore.QObject.connect(self.action_accountmanage, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.accountManage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "天才吧预约", None))
        self.gBListName.setTitle(_translate("MainWindow", "列表名", None))
        item = self.tWTaskList.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tWTaskList.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tWTaskList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "账号", None))
        item = self.tWTaskList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "进度", None))
        item = self.tWTaskList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "代理", None))
        item = self.tWTaskList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "零售店", None))
        item = self.tWTaskList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "服务类型", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "未完成", None))
        self.gBTaskName.setTitle(_translate("MainWindow", "列表名", None))
        item = self.tWComplete.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tWComplete.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tWComplete.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "账号", None))
        item = self.tWComplete.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "零售店", None))
        item = self.tWComplete.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "服务类型", None))
        item = self.tWComplete.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "代理", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_current), _translate("MainWindow", "完成", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "发送预约码", None))
        self.label_6.setText(_translate("MainWindow", "手机号：", None))
        self.label_7.setText(_translate("MainWindow", "预约码：", None))
        self.groupBox_15.setTitle(_translate("MainWindow", "验证码(双击刷新)", None))
        self.lbVerifyCodePic.setText(_translate("MainWindow", "TextLabel", None))
        self.groupBox_16.setTitle(_translate("MainWindow", "输入验证码", None))
        self.pBOk_2.setText(_translate("MainWindow", "确定", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_2.setTitle(_translate("MainWindow", "任务", None))
        self.menu_3.setTitle(_translate("MainWindow", "设置", None))
        self.menu_4.setTitle(_translate("MainWindow", "管理", None))
        self.menu_5.setTitle(_translate("MainWindow", "帮助", None))
        self.action.setText(_translate("MainWindow", "配置", None))
        self.action_2.setText(_translate("MainWindow", "开始任务", None))
        self.action_3.setText(_translate("MainWindow", "导入任务", None))
        self.action_4.setText(_translate("MainWindow", "任务列表", None))
        self.action_accountmanage.setText(_translate("MainWindow", "账号管理", None))
        self.action_6.setText(_translate("MainWindow", "关于", None))
        self.action_7.setText(_translate("MainWindow", "登录", None))
        self.action_9.setText(_translate("MainWindow", "更新代理列表", None))
        self.action_10.setText(_translate("MainWindow", "自定义代理", None))
        self.action_task_manage.setText(_translate("MainWindow", "任务管理", None))
        self.action_8.setText(_translate("MainWindow", "计划任务", None))
        self.action_11.setText(_translate("MainWindow", "代理管理", None))
        self.action_12.setText(_translate("MainWindow", "账号管理", None))
