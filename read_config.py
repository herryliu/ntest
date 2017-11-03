import sys
sys.path.append('/usr/lib/python2.7/dist-packages/')
print('\n'.join(sys.path))

from napalm_base import get_network_driver
import napalm_yang

import json
def pretty_print(dictionary):
        print(json.dumps(dictionary, sort_keys=True, indent=4))

#with open('./jpncore1.conf', 'r') as f:
with open('/gen/backup/net/leaf1-shn1a0239/current.conf', 'r') as f:
    config = f.read()

running_config = napalm_yang.base.Root()
running_config.add_model(napalm_yang.models.openconfig_interfaces)
running_config.parse_config(native=[config], profile=["eos"])

pretty_print(running_config.get(filter=True))
