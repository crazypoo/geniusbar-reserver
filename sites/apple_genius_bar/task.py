# -*- coding: utf-8 -*-
class Task(object):
    def __init__(self,
                 taskName,
                 storeName,
                 reservType,
                 proxyserver=None,
                 proxyport=80):

        self.taskName = taskName
        self.storeName = storeName
        self.reservType = reservType
        self.accounts = []
        self.proxyServer = proxyserver
        self.proxyPort = proxyport

    def addAccount(self, account):
        self.accounts.append(account)

    def getAccounts(self):
        return self.accounts

    def store(self):
        pass

    def retrieve(self):
        pass
