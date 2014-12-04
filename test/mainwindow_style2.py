import sys
sys.path.append('..')
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from gui.widgetitem import WidgetItem


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        workspace = QtGui.QWorkspace()
        self.setCentralWidget(workspace)
        self.id = 1
        te = QtGui.QTextEdit(self)
        self.setCentralWidget(te)
        for i in range(10):
            self.additem()

    def additem(self):
        dock = QtGui.QDockWidget()
        dock.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        dock.setFeatures(QtGui.QDockWidget.DockWidgetMovable)
        self.item = WidgetItem(self.id)
        self.id += 1
        dock.setWidget(self.item)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)

    def work__init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        workspace = QtGui.QWorkspace()
        self.setCentralWidget(workspace)
        self.id = 1
        self.item = WidgetItem(self.id)
        workspace.addWindow(self.item)
        self.item = WidgetItem(self.id+1)
        workspace.addWindow(self.item)

    def onOk(self):
        self.item = WidgetItem(self.id)
        workspace.addWindow(self.item)
        self.id += 1


def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()

main()
