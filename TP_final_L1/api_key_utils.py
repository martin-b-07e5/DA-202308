import configparser


def api_key_utils():
    # Crea un objeto ConfigParser
    config = configparser.ConfigParser()
    # Lee el archivo de configuración
    config.read('config.ini')

    # Obtén los valores de latitud, longitud y clave API del archivo de configuración config.ini
    # lat = config.getfloat('WeatherAPI', 'lat')
    # lon = config.getfloat('WeatherAPI', 'lon')
    api_key = config.get('WeatherAPI', 'api_key')

    # Devuelve los valores
    # return lat, lon, api_key
    return api_key
