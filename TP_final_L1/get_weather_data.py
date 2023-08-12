import requests


# This function retrieves weather data from an API by providing latitude, longitude and API key as input parameters.
# It returns the fetched data in JSON format if the request is successful, or displays an error message otherwise.
def get_weather_data(coords_list, api_key):
    # url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'
    # Line below is left to see the json structure.
    # url = f'https://api.openweathermap.org/data/2.5/weather?lat=-27.451100&lon=-58.986600&units=metric&appid=8c5a58462c901349b7c58423129a55dd'

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
            print("Error in API request:", str(e))
            print(
                f"Error obtaining data for lat={lat}, lon={lon}: {str(e)}")
        except Exception as e:
            print("An error occurred:", str(e))
            print(f"An error occurred for lat={lat}, lon={lon}: {str(e)}")

    return data_list
