# Get configuration from ini file relative to the py script

import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config
# Get URL property from chatGPT section of the config file

def get_property(section,property):
    config = get_config()
    return config[section][property]