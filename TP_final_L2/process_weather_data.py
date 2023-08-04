# process_weather_data.py

from datetime import datetime


# Returns a list of dictionaries with the processed data ready to be stored or used later.
# Each item in the list represents the data processed for a particular city.
def process_weather_data(data_list):
    processed_data_list = []

    for data in data_list:
        lat = data['lat']
        lon = data['lon']
        timezone = data['timezone']  # Timezone name
        timezone_offset = data['timezone_offset'] / 60 / 60
        # ----------------------------------------------------------------
        dt_current = datetime.fromtimestamp(data['current']['dt']).isoformat()
        sunrise_current = datetime.fromtimestamp(
            data['current']['sunrise']).time().isoformat()
        sunset_current = datetime.fromtimestamp(
            data['current']['sunset']).time().isoformat()
        temp_current = data['current']['temp']
        feels_like_current = data['current']['feels_like']
        pressure_current = data['current']['pressure']
        humidity_current = data['current']['humidity']  # Humidity, %
        dew_point_current = data['current']['dew_point']
        clouds_current = data['current']['clouds']  # Cloudiness, %
        visibility_current = data['current']['visibility']
        wind_speed_current = data['current']['wind_speed']
        wind_deg_current = data['current']['wind_deg']  # Wind direction
        rain_current = data['current']['rain']['1h'] if 'rain' in data['current'] else 0
        id_weather_current = data['current']['weather'][0]['id']
        # ----------------------------------------------------------------
        # Extract hourly weather data
        hourly_weather_list = []

        if 'hourly' in data:
            for hour_data in data['hourly']:
                dt_hourly = datetime.fromtimestamp(hour_data['dt']).isoformat()
                temp_hourly = hour_data['temp']
                feels_like_hourly = hour_data['feels_like']
                pressure_hourly = hour_data['pressure']
                humidity_hourly = hour_data['humidity']
                dew_point_hourly = hour_data['dew_point']
                clouds_hourly = hour_data['clouds']
                visibility_hourly = hour_data['visibility']
                wind_speed_hourly = hour_data['wind_speed']
                wind_deg_hourly = hour_data['wind_deg']
                rain_hourly = hour_data['rain']['1h'] if 'rain' in hour_data else 0
                id_weather_hourly = hour_data['weather'][0]['id']

                hourly_weather_data = {
                    'dt_hourly': dt_hourly,
                    'temp_hourly': temp_hourly,
                    'feels_like_hourly': feels_like_hourly,
                    'pressure_hourly': pressure_hourly,
                    'humidity_hourly': humidity_hourly,
                    'dew_point_hourly': dew_point_hourly,
                    'clouds_hourly': clouds_hourly,
                    'visibility_hourly': visibility_hourly,
                    'wind_speed_hourly': wind_speed_hourly,
                    'wind_deg_hourly': wind_deg_hourly,
                    'rain_hourly': rain_hourly,
                    'id_weather_hourly': id_weather_hourly
                }

                hourly_weather_list.append(hourly_weather_data)  # important
        # ----------------------------------------------------------------

        processed_data = {
            'lat': lat,
            'lon': lon,
            'timezone': timezone,
            'timezone_offset': timezone_offset,

            'dt_current': dt_current,
            'sunrise_current': sunrise_current,
            'sunset_current': sunset_current,
            'temp_current': temp_current,
            'feels_like_current': feels_like_current,
            'pressure_current': pressure_current,
            'humidity_current': humidity_current,
            'dew_point_current': dew_point_current,
            'clouds_current': clouds_current,
            'visibility_current': visibility_current,
            'wind_speed_current': wind_speed_current,
            'wind_deg_current': wind_deg_current,
            'rain_current': rain_current,
            'id_weather_current': id_weather_current,

            'hourly_weather': hourly_weather_list  # important
        }

        processed_data_list.append(processed_data)

    return processed_data_list
