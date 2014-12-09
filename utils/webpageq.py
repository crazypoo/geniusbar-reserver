# -*- coding: utf-8 -*-
from utils import debug

from PyQt4.QtCore import QUrl, QByteArray, QObject
from PyQt4.QtNetwork import QNetworkRequest


class WebPageQ(QObject):
    netWrokMgr = None

    def __init__(self, netWorkMgr):
        super(WebPageQ, self).__init__()
        self.netWorkMgr = netWorkMgr

    def open(self, url, post_data=None, headers={}, receiver=None):
        request = QNetworkRequest(QUrl(url))
        if post_data:
            debug.debug('post %s' % url)
            postData = QByteArray()
            for key, var in post_data.items():
                postData.append('%s=%s&' % (key, var))
            for header, var in headers.items():
                request.setRawHeader(header, var)
            reply = self.netWorkMgr.post(request, postData)
        else:
            debug.debug('get %s' % url)
            for header, var in headers.items():
                request.setRawHeader(header, var)
            reply = self.netWorkMgr.get(request)

        if receiver:
            reply.finished.connect(receiver)
        else:
            receiver = self.netWorkMgr.parent()
            reply.finished.connect(receiver.replyFinished)
