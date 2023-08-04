# save_weather_data.py

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from models import WeatherData, HourlyWeather


# Saves weather data in the database using SQLAlchemy.
def save_weather_data(engine, processed_data_list):
    try:
        SessionClass = sessionmaker(bind=engine)
        sessionObject = SessionClass()

        for processed_data in processed_data_list:
            weather_data = WeatherData(
                lat=processed_data['lat'],
                lon=processed_data['lon'],
                timezone=processed_data['timezone'],
                timezone_offset=processed_data['timezone_offset'],
                dt_current=processed_data['dt_current'],
                sunrise_current=processed_data['sunrise_current'],
                sunset_current=processed_data['sunset_current'],
                temp_current=processed_data['temp_current'],
                feels_like_current=processed_data['feels_like_current'],
                pressure_current=processed_data['pressure_current'],
                humidity_current=processed_data['humidity_current'],
                dew_point_current=processed_data['dew_point_current'],
                clouds_current=processed_data['clouds_current'],
                visibility_current=processed_data['visibility_current'],
                wind_speed_current=processed_data['wind_speed_current'],
                wind_deg_current=processed_data['wind_deg_current'],
                rain_current=processed_data['rain_current'],
                id_weather_current=processed_data['id_weather_current'],
            )

            hourly_weather_list = processed_data['hourly_weather']
            for hourly_data in hourly_weather_list:
                hourly_weather = HourlyWeather(
                    dt_hourly=hourly_data['dt_hourly'],
                    temp_hourly=hourly_data['temp_hourly'],
                    feels_like_hourly=hourly_data['feels_like_hourly'],
                    pressure_hourly=hourly_data['pressure_hourly'],
                    humidity_hourly=hourly_data['humidity_hourly'],
                    dew_point_hourly=hourly_data['dew_point_hourly'],
                    clouds_hourly=hourly_data['clouds_hourly'],
                    visibility_hourly=hourly_data['visibility_hourly'],
                    wind_speed_hourly=hourly_data['wind_speed_hourly'],
                    wind_deg_hourly=hourly_data['wind_deg_hourly'],
                    rain_hourly=hourly_data['rain_hourly'],
                    id_weather_hourly=hourly_data['id_weather_hourly'],
                )
                weather_data.hourly_weather.append(hourly_weather)

            sessionObject.add(weather_data)

        sessionObject.commit()

        print("Weather data successfully stored, from save_weather_data.py.")

    except Exception as e:
        print('An exception occurred:', e)
