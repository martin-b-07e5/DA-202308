import os
import pandas as pd
from datetime import datetime


def normalize_data(processed_data):
    # Normalizar el JSON
    df_normalized = pd.json_normalize(processed_data)

    # print("Imprimir el DataFrame sin mostrar los índices")
    # print(df_normalized.to_string(index=False))

    # Directorio donde se guardará el archivo CSV
    # Ruta absoluta del directorio actual
    current_directory = os.path.abspath(os.getcwd())
    # output_dir = os.path.join(current_directory, 'output')
    output_dir = os.path.join(current_directory, 'data_analytics/openweather')

    # Crear el directorio "output" si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Formatear la fecha actual en el nombre del archivo
    file_date = datetime.now().strftime('%Y-%m-%d')  # Ejemplo: 2023-07-24
    csv_file_name = f'tiempodiario_{file_date}.csv'

    # Ruta completa del archivo CSV
    csv_file_path = os.path.join(output_dir, csv_file_name)

    # Guardar el DataFrame en el archivo CSV en modo "append"
    # El argumento 'index=False' evita que se agreguen índices adicionales
    df_normalized.to_csv(csv_file_path, index=False, mode='a',
                         header=not os.path.exists(csv_file_path))
