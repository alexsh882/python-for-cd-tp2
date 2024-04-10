import sqlite3
import os

PATH_FILE_DATABASE = "db/"
FILE_DATABASE = "database.db"



def create_connection_sqlite3(db_file=FILE_DATABASE):

    if not os.path.exists(PATH_FILE_DATABASE+db_file):
        print("No existe la base de datos, se procede a crear el archivo.")
        open(PATH_FILE_DATABASE+db_file, "w")

    try:
        db = sqlite3.connect(PATH_FILE_DATABASE+db_file)
        print("Conexión exitosa a base de datos exitosa.")
        return db
    except sqlite3.Error as e:
        print(e)
    return None

db_instance = create_connection_sqlite3()

def get_db_instance():
    return db_instance

def create_table_localities(db=db_instance):
    try:
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS localities")
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS localities (
                id INTEGER,
                province TEXT NOT NULL,
                locality TEXT NOT NULL,
                postal_code TEXT NOT NULL DEFAULT '0000',
                id_prov_mstr INTEGER NOT NULL

            )
        """
        )
        db.commit()
        cursor.close()
    except sqlite3.Error as e:
        db.rollback()
        print(f"Error al crear la tabla: {e}")
        return None

