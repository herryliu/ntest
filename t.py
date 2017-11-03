from napalm_base import get_network_driver
import napalm_yang

import json

def use_mock_devices():
    cisco_configuration = {
        'hostname': '127.0.0.1',
        'username': 'vagrant',
        'password': '',
        'optional_args': {'path': "./junos_mock/", 'profile': ['junos'],
                          'increase_count_on_error': False}
    }

    eos_configuration = {
        'hostname': '127.0.0.1',
        'username': 'vagrant',
        'password': 'vagrant',
        'optional_args': {'path': "./eos_mock", 'profile': ['eos'],
                          'increase_count_on_error': False}
    }

    cisco = get_network_driver("mock")
    cisco_device = cisco(**cisco_configuration)

    eos = get_network_driver("mock")
    eos_device = eos(**eos_configuration)
    return cisco_device, eos_device

def use_real_devices():
    cisco_configuration = {
        'hostname': 'sha-netlab-1',
        'username': 'tim',
        'password': 'a',
        #'optional_args': {'port': 12203, 'config_lock': False}
    }

    eos_configuration = {
        'hostname': 'sha-netlab-6',
        'username': 'admin',
        'password': 'admin',
        #'optional_args': {'port': 12443}
    }

    cisco = get_network_driver("ios")
    cisco_device = cisco(**cisco_configuration)

    eos = get_network_driver("eos")
    eos_device = eos(**eos_configuration)
    return cisco_device, eos_device

def pretty_print(dictionary):
    print(json.dumps(dictionary, sort_keys=True, indent=4))

# Use real devices on your lab, tweak config
cisco_device, eos_device = use_real_devices()

# Use mocked devices intended for this test
#cisco_device, eos_device = use_mock_devices()

config = napalm_yang.base.Root()

# Adding models to the object
config.add_model(napalm_yang.models.openconfig_interfaces())
config.add_model(napalm_yang.models.openconfig_vlan())

pretty_print(napalm_yang.utils.model_to_dict(config))
