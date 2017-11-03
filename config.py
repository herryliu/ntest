from napalm_base import get_network_driver
import napalm_yang

import json

def pretty_print(dictionary):
    print(json.dumps(dictionary, sort_keys=True, indent=4))

# Use real devices on your lab, tweak config
#cisco_device, eos_device = use_real_devices()

# Use mocked devices intended for this test
#cisco_device, eos_device = use_mock_devices()

config = napalm_yang.base.Root()

# Adding models to the object
config.add_model(napalm_yang.models.openconfig_interfaces())
config.add_model(napalm_yang.models.openconfig_vlan())

pretty_print(napalm_yang.utils.model_to_dict(config))
