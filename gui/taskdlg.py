import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import multiprocessing
from multiprocessing import Process
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
        self.result = multiprocessing.Queue(1)
        self.appleGeniusBarReservation = AppleGeniusBarReservation()
        self.signalTaskCompleted.connect(self.finished)
        self.signalUpdateTaskProgress.connect(self.updataProcess)

    def startTask(self):
        self.ui.pBStartTask.setEnabled(False)
        task = Process(target=self.appleGeniusBarReservation.jump_login_page,
                       args=(self.enterUrl, self.result))

        status = multiprocessing.Queue(1)
        polling = threading.Thread(target=self.polling,
                                             args=(status, ))
        task.start()
        polling.start()

    def finished(self):
        verfiyData = self.result.get()
        if verfiyData:
            image = QtGui.QImage.fromData(verfiyData)
            pixmap = QtGui.QPixmap(image)
            size = QtCore.QSize(pixmap.width(), pixmap.height())
            self.ui.lbVerifyCodePic.resize(size)
            self.ui.lbVerifyCodePic.setPixmap(pixmap)
        else:
            debug.info('verifyData is none')

    def updataProcess(self, process):
        self.ui.progressBar.setValue(process)

    def polling(self, result):
        self.appleGeniusBarReservation.isCompleted(result)
        res = result.get()
        self.signalUpdateTaskProgress.emit(res[1])
        while not res[0]:
            print('startus %s process %s' % (res[0], res[1]))
            self.signalTaskCompleted.emit()
            self.signalUpdateTaskProgress.emit(res[1])
            time.sleep(1)
            self.appleGeniusBarReservation.isCompleted(result)
            res = result.get()


    def onOk(self):
        print('on accept')
