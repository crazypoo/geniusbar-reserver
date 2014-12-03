# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from utils import debug
debug.setLevel(10)
from gui import interface


if __name__ == '__main__':
    interface.main()
