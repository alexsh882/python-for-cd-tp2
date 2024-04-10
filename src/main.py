import time

from db.db_connection import create_table_localities
from src.features.create_csvs import create_csv_from_database
from src.features.insert_data_from_csv import read_and_insert_csv_data_to_database
  

def main():
    init_time = time.time()
    # crear la tabla localidades, incluye la conexión a la base de datos y la creación de la tabla.
    create_table_localities()
    # Leer el archivo localidades.csv y cargar los datos a la base de datos.
    read_and_insert_csv_data_to_database()
    # Crear los archivos csv de cada provincia con sus localidades.
    create_csv_from_database()
    end_time = time.time()
    # Agregué un timer para verificar el tiempo que demora todo esto.
    print(f"Tiempo de ejecución: {(end_time - init_time):.2} segundos.")
