import sys
#sys.path.append('/usr/lib/python2.7/dist-packages/')
from napalm_base import get_network_driver
import napalm_yang

import json


print('\n'.join(sys.path))


def pretty_print(dictionary):
    print(json.dumps(dictionary, sort_keys=True, indent=4))

def use_real_devices():
    '''
    cisco_configuration = {
        'hostname': 'sha-netlab-1',
        'username': 'admin',
        'password': 'admin',
    }
    '''

    eos_configuration = {
        'hostname': 'sha-netlab-6',
        'username': 'tim',
        'password': 'a',
    }
    '''
    cisco = get_network_driver("ios")
    cisco_device = cisco(**cisco_configuration)
    '''

    eos = get_network_driver("eos")
    eos_device = eos(**eos_configuration)
    #return cisco_device, eos_device
    return eos_device

#cisco_device, eos_device = use_real_devices()
eos_device = use_real_devices()

# test the device

with eos_device as d:
    print d.get_facts()
config = eos_device.get_config()
print(config)
'''
with cisco_device as d:
    print d.get_facts()
'''
config_file = open('/gen/backup/net/jpncore1/current.conf').read()
running_config = napalm_yang.base.Root()
running_config.add_model(napalm_yang.models.openconfig_interfaces)
#running_config.parse_config(native=config['running'], profile=['eos'])
running_config.parse_config(native=config['running'].split('\n'), profile=['eos'])
#running_config.parse_config(native=config, profile=['eos'])
#running_config.parse_config(device=eos_device, profile=['eos'])

#running_config.parse_config(native=config_file.split('\n'), profile=['eos'])
pretty_print(running_config.get(filter=True))
#pretty_print(napalm_yang.utils.model_to_dict(running_config))
