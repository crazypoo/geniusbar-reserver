import sys
sys.path.append('../sites/')
sys.path.append('..')
from utils import debug
debug.setLevel(10)

from sites.apple_main import AppleGeniusBarReservation
from utils import CommandLine

appleGeniusBarReservation = AppleGeniusBarReservation()
stores = AppleGeniusBarReservation.Init_stores_list()
for index, (key, value) in stores.items():
    pass

#index = input("Select a store: ")
index = 1
store_url = AppleGeniusBarReservation.Get_store_url((stores[int(index)][1]))
supporturl= AppleGeniusBarReservation.Get_suppport_url(store_url)
appleGeniusBarReservation = AppleGeniusBarReservation()
appleGeniusBarReservation.jump_login_page(supporturl)

