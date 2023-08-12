import configparser


def api_key_utils():
    # Create a ConfigParser object.
    config = configparser.ConfigParser()
    # Read the configuration file.
    config.read('config.ini')

    # Get API key from config.ini file
    api_key = config.get('WeatherAPI', 'api_key')

    return api_key
