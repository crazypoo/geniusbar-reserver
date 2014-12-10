import sys
if '../' not in sys.path:
    sys.path.append('../')
from sites.apple_main import AppleGeniusBarReservation
from sites.apple_genius_bar.store_page import GeniusbarPage



def test_timeslotpage():
    appleGeniusBarReservation = AppleGeniusBarReservation({})
    page = GeniusbarPage('')
    f = open('timeslots.htm', 'r')
    data = f.read()
    f.close()
    data = data.encode('utf-8', 'ignore').replace('&nbsp', '').encode('utf-8')
    ret = appleGeniusBarReservation.buildTimeSlotsTable(page, data)

    for r in ret:
        for name, times in r.items():
            print(name)
            for time, id in times:
                print(time)
test_timeslotpage()
