import requests


# Esta función obtiene los datos meteorológicos de una API proporcionando la latitud, longitud y clave de API como parámetros de entrada.
# Devuelve los datos obtenidos en formato JSON si la solicitud se realiza correctamente, o muestra un mensaje de error en caso contrario.
def get_weather_data(coords_list, api_key):
    # url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    # dejado solo para ver el json
    # url = f'https://api.openweathermap.org/data/2.5/weather?lat=-27.451100&lon=-58.986600&units=metric&appid=b150a2ad5241d00777be4fc3e0fc946c'

    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    data_list = []

    for lat, lon in coords_list:
        params = {
            'lat': lat,
            'lon': lon,
            'appid': api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            data_list.append(data)
        except requests.exceptions.RequestException as e:
            print("Error al realizar la solicitud a la API:", str(e))
            print(
                f"Error al obtener los datos para lat={lat}, lon={lon}: {str(e)}")
        except Exception as e:
            print("Ocurrió un error:", str(e))
            print(f"Ocurrió un error para lat={lat}, lon={lon}: {str(e)}")

    return data_list
