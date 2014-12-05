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

    def getAccounts(self):
        jsonhelper = JsonHelper(self.fileName)
        objs = jsonhelper.objs()
        if objs:
            return objs
        return {}

    def addAccounts(self, accounts={}):
        jsonhelper = JsonHelper(self.fileName)
        jsonhelper.write_objs(accounts)
