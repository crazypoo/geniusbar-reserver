# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialog
from uidesigner.ui_tasklistdlg import Ui_TaskListDLG


class TaskListDLG(QDialog):
    def __init__(self, appContext, parent=None):
        super(TaskListDLG, self).__init__(parent)
        self.ui = Ui_TaskListDLG()
        self.ui.setupUi(self)
        self.appContext = appContext
        self.selectedTask = []
        sig = self.ui.listWidget.signalCellContextMenu
        sig.connect(self.contextMenuEvent)
        self.initUI()

    def contextMenuEvent(self, event):
        pass

    def showEvent(self, event):
        self.initUI()

    def initUI(self):
        self.ui.listWidget.clear()
        tasks = self.appContext.taskManageDLG.tasks
        for taskName, _ in tasks.items():
            self.ui.listWidget.addItem(taskName)

    def _getTasks(self):
        items = self.ui.listWidget.selectedItems()
        result = []
        tasks = self.appContext.taskManageDLG.tasks
        for item in items:
            taskName = str(item.text())
            for taskname, task in tasks.items():
                if taskName == taskname:
                    result.append(task)
                    break
        return result

    def getTasks(self):
        selectedTask = self.selectedTask
        self.selectedTask = None
        return selectedTask

    def accept(self):
        self.selectedTask = self._getTasks()
        super(TaskListDLG, self).accept()
