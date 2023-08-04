# api_key_utils.py

import configparser


def api_key_utils():
    config = configparser.ConfigParser()    # Creates a ConfigParser object
    config.read('config.ini')    # Read the configuration file
    api_key = config.get('WeatherAPI', 'api_key')

    return api_key
