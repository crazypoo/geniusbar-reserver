import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from multiprocessing import Process, Manager
import threading
import time
from uidesigner.ui_taskdlg import Ui_TaskDialog
from sites.apple_main import AppleGeniusBarReservation
from utils import debug


class TaskDLG(QtGui.QDialog):
    signalTaskCompleted = QtCore.pyqtSignal()
    signalUpdateTaskProgress = QtCore.pyqtSignal(int)

    def __init__(self, enterUrl,
                 loginData,
                 taskId=1, parent=None):

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
        self.loginData = loginData
        self.initLoginDataUi()
        self.appleGeniusBarReservation = AppleGeniusBarReservation(loginData)
        self.signalTaskCompleted.connect(self.finished)
        self.signalUpdateTaskProgress.connect(self.updataProcess)
        print(self.loginData)

    def initLoginDataUi(self):
        self.ui.combServType.addItem(self.loginData['reservType'])
        storename = unicode(self.loginData['storeName'], 'utf8', 'ignore')
        self.ui.combStore.addItem(QtCore.QString(storename))
        self.ui.lEGovId.setText(self.loginData['governmentID'])
        self.ui.lEPhoneNumber.setText(self.loginData['phoneNumber'])
        self.ui.lEPasswd.setText(self.loginData['accountPassword'])
        self.ui.lEUserName.setText(self.loginData['appleId'])
        self.ui.lEReservCode.setText(self.loginData['reservCode'])

    def startTask(self):
        self.taskStatus = Manager().dict()
        self.taskStatus['verifyCodeData'] = None
        self.taskStatus['taskProgress'] = 0
        self.taskStatus['prompInfo'] = None
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
            self.ui.pTSm
        else:
            debug.info('verifyData is none')

    def updataProcess(self, progress):
        val = self.ui.progressBar.value()
        if not val == progress:
            self.ui.progressBar.setValue(progress)

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
