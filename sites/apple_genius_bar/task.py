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
        # 0 is no changed ,1 have changed
        self.status = 0

    def addAccount(self, accounts):
        self.accounts.extend(accounts)

    def setAccounts(self, accounts):
        self.accounts = accounts

    def getAccounts(self):
        return self.accounts

    def updateAccount(self, account):
        for index, ac in enumerate(self.accounts):
            if ac['appleid'] == account['appleid']:
                del self.accounts[index]
                self.accounts.append(account)
                break

    def getAccount(self, appleId):
        for index, ac in enumerate(self.accounts):
            if ac['appleid'] == appleId:
                return (ac, index)

    def store(self):
        pass

    def retrieve(self):
        pass
