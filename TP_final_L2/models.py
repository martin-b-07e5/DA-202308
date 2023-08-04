# models.py

from datetime import datetime, timedelta
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Creating a declarative base class for ORM classes
Base = declarative_base()


class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    lat = Column(Float)
    lon = Column(Float)
    timezone = Column(String)
    timezone_offset = Column(Float)

    dt_current = Column(String)
    sunrise_current = Column(Integer)
    sunset_current = Column(Integer)
    temp_current = Column(Float)
    feels_like_current = Column(Float)
    pressure_current = Column(Float)
    humidity_current = Column(Float)
    dew_point_current = Column(Float)
    clouds_current = Column(Float)
    visibility_current = Column(Float)
    wind_speed_current = Column(Float)
    wind_deg_current = Column(Float)
    rain_current = Column(Float)
    id_weather_current = Column(Integer)
    # each time a new instance of WeatherData is created, the lambda function will be called and the current time will be obtained.
    created_at = Column(DateTime, default=lambda: datetime.now())

    hourly_weather = relationship(
        'HourlyWeather', back_populates='weather_data')


class HourlyWeather(Base):
    __tablename__ = 'hourly_weather'
    id = Column(Integer, primary_key=True)
    weather_data_id = Column(Integer, ForeignKey('weather_data.id'))
    dt_hourly = Column(String)
    temp_hourly = Column(Float)
    feels_like_hourly = Column(Float)
    pressure_hourly = Column(Float)
    humidity_hourly = Column(Float)
    dew_point_hourly = Column(Float)
    clouds_hourly = Column(Float)
    visibility_hourly = Column(Float)
    wind_speed_hourly = Column(Float)
    wind_deg_hourly = Column(Float)
    rain_hourly = Column(Float)
    id_weather_hourly = Column(Integer)

    weather_data = relationship('WeatherData', back_populates='hourly_weather')


""" In SQLAlchemy, the use of lambda in the default expression allows you
to specify an anonymous function that will automatically call
to get the default value of the column
when a new record is inserted into the table.

In this specific case, lambda: datetime.now()
  creates an anonymous function with no arguments
  that returns the current value of the datetime object
That is, the current date and time, at the time the record is inserted into the database.
"""
