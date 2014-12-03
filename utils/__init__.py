# -*- coding: utf-8 -*-
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def Writefile(filename, data):
    debug.debug('write %s' % filename)
    with open(filename, "w") as f:
        f.write(data)


class Debug():
    '''
    Debug info print( and write the log into files
    '''
    def __init__(self, logfile):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(20)
        self.level = 20
        formatter = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s', '%a, %d %b %Y %H:%M:%S',)  
        file_handler = logging.FileHandler(logfile)
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler(sys.stderr)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)
        self.uiOutputSignal = None
        self.uiOutputLevel = 1

    def setOutputSignal(self, outputSignal):
        self.uiOutputSignal = outputSignal

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.logger.setLevel(level)
        self.level = level

    def __call__(self, msg):
        self.logger.debug(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)
        if self.uiOutputLevel >= 1 and self.uiOutputSignal:
            self.uiOutputSignal.emit(msg)

    def error(self, msg):
        self.logger.error(msg)

    def output(self, msg):
        self.logger.debug(msg)

debug = Debug("run.log")


class CommandLine(object):
    def parseCmdLine(self):

        import optparse
        usage = "usage: %prog [options] arg"
        parser = optparse.OptionParser(usage)
        parser.add_option('-s', '--store', dest='store name',
                          help='store name')
        
        parser.add_option('-l', '--list', dest='list store name',
                          help='list store name')
        return parser.parse_args()


# ############################################
import json


class JsonHelper():
    def __init__(self, jsonfile):
        self.filename = jsonfile

    def data(self):
        try:
            with open(self.filename, 'r') as f:
                data = f.read()
                return data
        except Exception as e:
            debug.info('Can not open %s' % self.filename)

    def objs(self):
        data = self.data()
        if data:
            objs = json.loads(data)
        else:
            objs = None
        return objs

    def write_objs(self, objs):
        try:
            with open(self.filename, 'w') as f:
                enObjs = json.dumps(objs)
                f.write(enObjs)
        except Exception as e:
            debug.error('Can not write %s ,%s' % (self.filename, str(e)))
