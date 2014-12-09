import sys
sys.path.append('..')
from utils.webpageq import WebPageQ
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import QUrl
import time
from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest
headers = {}
headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
headers["Connection"] = 'keep-alive'


class MyMain(QMainWindow):
    def __init__(self, parent=None):
        super(MyMain, self).__init__(parent)

    def readPage(self):
        #webpage = WebPageQ(url, headers=headers)
        #webpage.readPage()
       url = "http://www.apple.com/cn/retail/storelist/"
       WebPageQ.InitNetWorkAcesMgr(self)
       # request = QNetworkRequest(QUrl(url))
       # reply = WebPageQ.netWrokMgr.get(request)
       # reply.finished.connect(self.replayFinished)
       p = WebPageQ(url, headers)
       p.readPage()
    def replayFinished(self):
        print('sender')
        print(self.sender())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    url = "http://www.apple.com/cn/retail/storelist/"
    webpage = MyMain()
    webpage.show()
    webpage.readPage()
    app.exec_()
