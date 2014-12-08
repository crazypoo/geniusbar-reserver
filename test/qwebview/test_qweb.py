from PyQt4.QtGui import QDialog
from PyQt4.QtCore import QUrl, QString, QTextCodec
from qwebview import Ui_Dialog
import sys
from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt4.QtGui import QApplication, QMainWindow


class MyWebView(QDialog):
    def __init__(self, parent=None):
        super(MyWebView, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.webView.load(QUrl('http://www.apple.com/cn/retail/shanghaiiapm/'))
        page = self.ui.webView.page()
        print(page)

        
class MainWindow(QDialog):
    def __init__(self, parent=None):
       # super(MainWindow, self).__init__(parent)
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.manager = QNetworkAccessManager(self)
        request = QNetworkRequest()
        request.setUrl(QUrl('http://www.apple.com/cn/retail/shanghaiiapm/'))
        reply = self.manager.get(request)
        reply.finished.connect(self.replyFinished)
        self.ui.webView.load(request)

    def replyFinished(self):
        reply = self.sender()
        raw = reply.readAll()
        print(type(raw))
        print(type(str(raw).decode('ascii', 'ignore')))
        #print(str(raw.data()).decode('unicode', 'ignore'))
        #text = QTextCodec.codecForMib(1013).toUnicode(raw.data())
        # print(text)

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    exit(app.exec_())
    
if __name__ == "__main__":
    main()
