import json
import sys
sys.path.append('..')
from utils import JsonHelper


objs = {'1': {'name': 'name_1', 'phone_number': '123434'},
       '2': {'name': 'name_2', 'phone_number': '456789'}}

#encodejson = json.dumps(obj)
jsonhelper = JsonHelper('jsonfile.dat')
jsonhelper.write_objs(objs)

jsonhelper = JsonHelper('jsonfile.dat')
objs = jsonhelper.objs()
print(objs['1']['name'])
print(len(objs))


objs['3']={'name':'name_3', 'phone_number':'33333333333'}
jsonhelper.write_objs(objs)

jsonhelper = JsonHelper('jsonfile.dat')
objs = jsonhelper.objs()
print(objs['3']['name'])
print(len(objs))

