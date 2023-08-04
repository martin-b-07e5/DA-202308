from datetime import datetime, timedelta


# Esta función procesa los datos meteorológicos obtenidos de la API y extrae
#  la información relevante, como la temperatura, descripción, etc.
# Devuelve un diccionario con los datos procesados listos para ser almacenados o utilizados posteriormente.
# Devuelve un diccionario que contiene los datos obtenidos de la API del clima.
def process_weather_data(weather_data_list):
    processed_data_list = []

    for data in weather_data_list:

        temp = data['main']['temp']
        description = data['weather'][0]['description']
        city = data['name']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']

        my_timezone = data['timezone'] / 60 / 60

        sunrise_utc = int(data['sys']['sunrise'])
        sunset_utc = int(data['sys']['sunset'])
        dt_utc = int(data['dt'])

        # solo la hora
        sunrise_local = datetime.fromtimestamp(sunrise_utc).time().isoformat()
        sunset_local = datetime.fromtimestamp(sunset_utc).time().isoformat()
        # dt_local = datetime.fromtimestamp(dt_utc).time().isoformat()

        # Obtener el objeto datetime completo
        dt_local_datetime = datetime.fromtimestamp(dt_utc)

        # Restar tres horas al valor de dt_local_datetime
        dt_colab = (
            dt_local_datetime - timedelta(hours=3)).isoformat()

        processed_data = {
            'city': city,
            'temp': temp,
            'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max,
            'my_timezone': my_timezone,
            'sunrise_local': sunrise_local,
            'sunset_local': sunset_local,
            # 'dt_local': dt_local,
            'dt_local_datetime': dt_local_datetime,
            'dt_colab': dt_colab
        }

        processed_data_list.append(processed_data)

    return processed_data_list
