import sys
sys.path.append('../sites/')
sys.path.append('..')
from utils import debug
debug.setLevel(10)

from sites.apple_main import AppleGeniusBarReservation
from utils import CommandLine

appleGeniusBarReservation = AppleGeniusBarReservation()
stores = appleGeniusBarReservation.init_stores_list().get_store_list()
for index, (key, value) in stores.items():
    pass
#print('%d: %s %s' % (index, key, value))

#index = input("Select a store: ")
index = 1
store_url = appleGeniusBarReservation.get_store_url((stores[int(index)][1]))
supporturl=appleGeniusBarReservation.get_suppport_url(store_url)
appleGeniusBarReservation.jump_login_page(supporturl)

