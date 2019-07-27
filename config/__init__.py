import configparser
import json
import os
from fusenet.docker.logger import get_logger

log = get_logger(__name__)

config = configparser.ConfigParser()
script_dir = os.path.dirname(__file__)


def _parse_config(path: str):
    ret_data = {'DEFAULT': {}}

    with open(path) as json_data:
        data = json.load(json_data)
        for key, val in data.items():
            if type(val) is dict:
                ret_data[key] = val
            else:
                ret_data['DEFAULT'][key] = val

    return ret_data


def get_config(env: str = 'DEFAULT'):
    config.read_dict(_parse_config(os.path.join(script_dir, 'config.default.json')))

    if env != 'DEFAULT':
        overridefile = os.path.abspath(os.path.join(script_dir, '../..', 'config.%s.json' % env.lower()))
        if not os.path.isfile(overridefile):
            log.warning("Config file %s not found, using default" % overridefile)
        else:
            config.read_dict(_parse_config(overridefile))

    return config
