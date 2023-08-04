# get_weather_data.py

import requests
from five_days_ago import calculate_five_days_ago


# This function retrieves weather data from an API, taking latitude, longitude, and API key as input parameters.
# It returns the obtained data in JSON format
def get_weather_data(coords_list, api_key):
    # documentation: https://openweathermap.org/api/one-call-api#history'
    # base_url = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=-27.451100&lon=-58.986600&dt=1690856797&units=metric&lang=en&appid=8c5a58462c901349b7c58423129a55dd'

    base_url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'
    data_list = []

    # Call the function to obtain the value of "dt" minus 5 days.
    # _, _, timestamp_five_days_ago = calculate_five_days_ago()    # tuple of three elements
    # tuple of four elements
    current_date, five_days_ago, timestamp_five_days_ago, timestamps = calculate_five_days_ago()
    print("current_date:", current_date)
    print("five_days_ago:", five_days_ago)
    print("timestamp_five_days_ago:", timestamp_five_days_ago)
    print("timestamps:", timestamps, "\n")

    # scroll through the 5-day list
    for timestamp in timestamps:
        # Make API calls for each location (lat, lon) in the coords_list
        # https://openweathermap.org/api/one-call-api#history-how
        for lat, lon in coords_list:
            params = {
                'lat': lat,
                'lon': lon,
                'dt': timestamp,
                'appid': api_key,
                'units': 'metric',
                'lang': 'en'
            }
            try:
                response = requests.get(base_url, params=params)
                data = response.json()
                data_list.append(data)
            except requests.exceptions.RequestException as e:
                print("Error when making the API request:", str(e))
            except Exception as e:
                print("An error has occurred.:", str(e))

    return data_list
