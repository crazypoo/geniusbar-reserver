from PyQt4.QtGui import QWidget
from PyQt4.QtNetwork import QNetworkAccessManager
from PyQt4.QtNetwork import QNetworkCookieJar
from utils.webpageq import WebPageQ
from uidesigner.ui_taskviewwidget import Ui_Form
from PyQt4.QtCore import QUrl, QString
from PyQt4.QtNetwork import QNetworkRequest
from utils import Writefile
import threading
import multiprocessing
import time


class TaskViewWidget(QWidget):

    def __init__(self, parent=None):
        super(TaskViewWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def do(self, event):
        print('do')
        time.sleep(3)
        print('event set')
        event.set()

    def open(self, url=None):
        self.netWorkMgr = QNetworkAccessManager(self)
        cookieJar = QNetworkCookieJar()
        self.netWorkMgr.setCookieJar(cookieJar)

        event = threading.Event()
        p = threading.Thread(target=self.do, args=(event,))
        p.start()
        ret = event.wait(4)
        print(ret)
        print('nextStep')

    def startReserver(self, url=None, data=None, headers={}):
        #self.startReserver(url)
        return
        # request = QNetworkRequest()
        # request.setUrl(QUrl('http://www.apple.com/cn/retail/shanghaiiapm/'))
        # reply = self.netWorkMgr.get(request)
        # reply.finished.connect(self.replyFinished)
        url = 'http://www.apple.com/cn/retail/shanghaiiapm/'
        headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        headers["Connection"] = 'keep-alive'
        page = WebPageQ(self.netWorkMgr)
        page.open(url, headers=headers)
        #reply.finished.connect(self.replyFinished)
        #self.nextStep.wait()

        print('nextStep')

    def replyFinished(self):
        print('finished reading')
        reply = self.sender()
        data = reply.readAll()
        self.data = str(data).decode('ascii', 'ignore').encode('utf-8')
        #print(self.data)
        Writefile('store.htm', self.data)
