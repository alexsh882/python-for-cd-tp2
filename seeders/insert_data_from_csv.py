from read_data import read_csv
from db_connection import get_db_instance, create_table_localities

PATH_CSV_LOCALITIES = "./localidades.csv"


def read_and_insert_csv_data_to_database():
    data = read_csv(PATH_CSV_LOCALITIES)
    if data:
        insert_data_in_database(data)

def insert_data_in_database(data):
    db = get_db_instance()
    cur = db.cursor()
    try:
        if db:
            for row in data:
                cur.execute(
                    """
                    INSERT INTO localities (id, province, locality, postal_code, id_prov_mstr) 
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        row["id"],
                        row["provincia"],
                        row["localidad"],
                        row["cp"],
                        row["id_prov_mstr"],
                    ),
                )
            db.commit()
            cur.close()
    except Exception as e:
        db.rollback()
        print(f"Error al insertar los datos: {e}")