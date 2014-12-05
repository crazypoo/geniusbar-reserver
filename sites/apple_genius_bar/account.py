# -*- coding: utf-8 -*-
class Account(object):
    def __init__(self, data):

        self.data = data

    def getData(self):
        return {self.data['appleId']: self.data}
