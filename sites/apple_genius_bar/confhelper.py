from utils import JsonHelper


class ConfHelper():
    def addAccounts(self, filename, accounts={}):
        jsonhelper = JsonHelper(filename)
        jsonhelper.write_objs(accounts)
        print(accounts)

    def getAccounts(self, filename):
        jsonhelper = JsonHelper(filename)
        objs = jsonhelper.objs()
        if objs:
            return objs
        return {}
