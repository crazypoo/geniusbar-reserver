# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from sites.apple_genius_bar.store_page import GeniusbarPage

def test_challenge_phone_info():
    challenge = GeniusbarPage(None)
    f = open('smschallenge.htm', 'r')
    data = f.read()
    f.close()
    text = challenge.get_smschalleng_steps(data)
    print(text)
    
test_challenge_phone_info()
