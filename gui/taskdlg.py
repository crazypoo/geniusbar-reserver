import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from multiprocessing import Process, Manager
import threading
import time
from ui_taskdlg import Ui_TaskDialog
from sites.apple_main import AppleGeniusBarReservation
from utils import debug


class TaskDLG(QtGui.QDialog):
    signalTaskCompleted = QtCore.pyqtSignal()
    signalUpdateTaskProgress = QtCore.pyqtSignal(int)

    def __init__(self, enterUrl, taskId=1, parent=None):
        super(TaskDLG, self).__init__(parent)
        self.enterUrl = enterUrl
        self.ui = Ui_TaskDialog()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.image = QtGui.QImage()
        self.image.load('data/img.jpg')
        qpixmap = QtGui.QPixmap.fromImage(self.image)
        size = QtCore.QSize(qpixmap.width(), qpixmap.height())
        self.ui.lbVerifyCodePic.resize(size)
        self.ui.lbVerifyCodePic.setPixmap(qpixmap)
        self.taskId = taskId
        self.appleGeniusBarReservation = AppleGeniusBarReservation()
        self.signalTaskCompleted.connect(self.finished)
        self.signalUpdateTaskProgress.connect(self.updataProcess)

    def startTask(self):
        self.taskStatus = Manager().dict()
        self.taskStatus['verifyCodeData'] = None
        self.taskStatus['taskProgress'] = 0
        self.ui.pBStartTask.setEnabled(False)
        task = Process(target=self.appleGeniusBarReservation.jump_login_page,
                       args=(self.enterUrl, self.taskStatus))

        polling = threading.Thread(target=self.polling, args=())
        task.start()
        polling.start()

    def finished(self):
        verifyCodeData = self.taskStatus['verifyCodeData']
        if verifyCodeData:
            image = QtGui.QImage.fromData(verifyCodeData)
            pixmap = QtGui.QPixmap(image)
            size = QtCore.QSize(pixmap.width(), pixmap.height())
            self.ui.lbVerifyCodePic.resize(size)
            self.ui.lbVerifyCodePic.setPixmap(pixmap)
        else:
            debug.info('verifyData is none')

    def updataProcess(self, progress):
        val = self.ui.progressBar.value()
        if not val == progress:
            self.ui.progressBar.setValue(progress)
            print('updataProcess %s' % progress)

    def polling(self):
        progress = self.taskStatus['taskProgress']
        while progress < 100:
            self.signalUpdateTaskProgress.emit(progress)
            time.sleep(2)
            progress = self.taskStatus['taskProgress']
        self.signalUpdateTaskProgress.emit(progress)
        self.signalTaskCompleted.emit()

    def onOk(self):
        print('on accept')
