from utils import JsonHelper


class ConfHelper():
    def addItems(self, filename, accounts={}):
        jsonhelper = JsonHelper(filename)
        jsonhelper.write_objs(accounts)

    def getItems(self, filename):
        jsonhelper = JsonHelper(filename)
        objs = jsonhelper.objs()
        if objs:
            return objs
        return {}


class AccountManager(object):
    def __init__(self, filename):
        self.fileName = filename
        self.jsonhelper = JsonHelper(self.fileName)
        self.accounts = self._getAccounts()

    def getAccounts(self):
        if self.accounts:
            self.accounts
        return self._getAccounts()

    def _getAccounts(self):
        objs = self.jsonhelper.objs()
        if objs:
            return objs
        return {}

    def addAccounts(self, accounts={}):
        if not self.accounts:
            self.accounts = self._getAccounts()
        self.accounts = dict(self.accounts, **accounts)
        self.jsonhelper.write_objs(self.accounts)

    def getAccount(self, appleId):
        accounts = self.getAccounts()
        for id, account in accounts.items():
            if appleId in account.values():
                return account
