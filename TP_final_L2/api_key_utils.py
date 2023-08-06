# api_key_utils.py

import configparser
import os

def api_key_utils():
    config = configparser.ConfigParser()    # Creates a ConfigParser object
    # config.read('config.ini')    # Read the configuration file
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    api_key = config.get('WeatherAPI', 'api_key')

    return api_key
