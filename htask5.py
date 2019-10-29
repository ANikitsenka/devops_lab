import os
import sys
import pip
import site
import json
import yaml
from pip._internal.utils.misc import get_installed_distributions


dict_slave = dict()
dict_master = dict()
dict_master['Python version:'] = sys.version[0:5]
dict_master['Virtual environment:'] = os.environ['VIRTUAL_ENV']
dict_master['Python executable:'] = sys.executable
dict_master['PIP version:'] = pip.__version__
dict_master['PYTHONPATH:'] = os.environ['PYTHONPATH']
dict_master['Installed packs:'] = site.getsitepackages()

p = get_installed_distributions()
j = 0
for i in p:
    dict_slave[p[j].key] = p[j].version
    j += 1

dict_master['Packs_versions'] = dict_slave

with open('info.json', 'w') as outfile:
    json.dump(dict_master, outfile, indent=4)

with open('info.yaml', 'w') as file:
    yaml.dump(dict_master, file)
