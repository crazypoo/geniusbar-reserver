import sys
if '../' not in sys.path:
    sys.path.append('../')
from sites.apple_main import AppleGeniusBarReservation
from sites.apple_genius_bar.store_page import GeniusbarPage

import sys
reload(sys)
import os
sys.setdefaultencoding('utf-8')
cwd = os.path.abspath(os.getcwd())
# sites
sys.path.append(os.path.join(cwd, '../gui'))
sys.path.append(os.path.join(cwd, '../proxy'))
sys.path.append(os.path.join(cwd, '../sites'))
sys.path.append(os.path.join(cwd, '../utils'))

def test_timeslotpage():
    appleGeniusBarReservation = AppleGeniusBarReservation({})
    page = GeniusbarPage('')
    f = open('timeslots.htm', 'r')
    data = f.read()
    f.close()
    data = data.encode('utf-8', 'ignore')
    ret, maxrow = appleGeniusBarReservation.buildTimeSlotsTable(page, data)
    return ret, maxrow

#test_timeslotpage()
# -*- coding: utf-8 -*-
import sys
import os
from PyQt4 import QtGui
from gui.uidesigner.taskviewwidget import TaskViewWidget


def main(proxyServers=None):
    data, maxrow = test_timeslotpage()
    app = QtGui.QApplication(sys.argv)
    main = TaskViewWidget()
    main.fillTableWidget(data, maxrow)
    main.show()
    app.exec_()

if __name__ == "__main__":
    main()
