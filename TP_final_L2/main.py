# main.ipynb

from database_utils import create_engine_instance, create_database_tables
from api_key_utils import api_key_utils
from coords_list import coords_list
from get_weather_data import get_weather_data
from process_weather_data import process_weather_data
from save_weather_data import save_weather_data


def main():
    # ----------------------------------------------------------------------
    # 👷CREATE AN ENGINE INSTANCE for the database.
    db_folder = "DB_folder"
    db_name = "nivel_medio.db"
    engine = create_engine_instance(db_folder, db_name)

    # 👷CREATE ALL THE TABLES defined in the database schema.
    create_database_tables(engine)
    # ----------------------------------------------------------------------
    # ✅GET THE API KEY.
    api_key = api_key_utils()
    # ----------------------------------------------------------------------
    # ✅get_weather_data

    # List to store the weather data OF ALL CITIES.
    all_weather_data_list = []

    for lat, lon in coords_list:
        weather_data_list = get_weather_data([(lat, lon)], api_key)

        if weather_data_list:
            all_weather_data_list.extend(weather_data_list)
        else:
            print(f"Failed to fetch data for Lat={lat}, Lon={lon}")

    # print("Complete JSON:", all_weather_data_list)
    # ----------------------------------------------------------------------
    # ✅process_weather_data

    if weather_data_list:
        processed_data_list = process_weather_data(all_weather_data_list)
        # print("Filtered JSON.:", processed_data_list)
    # ----------------------------------------------------------------------
    # ✅save_weather_data

    if weather_data_list:
        save_weather_data(engine, processed_data_list)  # 0k works
    # ----------------------------------------------------------------------


if __name__ == '__main__':
    main()
