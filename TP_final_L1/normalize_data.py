import os
import pandas as pd
from datetime import datetime


def normalize_data(processed_data):
    # Normalize the JSON
    df_normalized = pd.json_normalize(processed_data)

    # print("Print the DataFrame without displaying the indexes")
    # print(df_normalized.to_string(index=False))

    # Directory where the CSV file will be saved.
    # Absolute path of the current directory.
    current_directory = os.path.abspath(os.getcwd())
    output_dir = os.path.join(current_directory, 'data_analytics/openweather')

    # Create the "output_dir" directory if it does not exist.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Format the current date in the file name.
    file_date = datetime.now().strftime('%Y-%m-%d')  # 2023-07-24
    csv_file_name = f'tiempodiario_{file_date}.csv'

    # Full path to the CSV file.
    csv_file_path = os.path.join(output_dir, csv_file_name)

    # Save the DataFrame in the CSV file in "append" mode.
    # The 'index=False' argument prevents additional indexes from being added.
    df_normalized.to_csv(
        csv_file_path,
        index=False,
        mode='a',
        header=not
        os.path.exists(csv_file_path)
    )
