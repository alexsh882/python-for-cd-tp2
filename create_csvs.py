from db_connection import get_db_instance
import csv


def create_csv_from_database():
    db = get_db_instance().cursor()
    try:
        if db:
            resp = db.execute(
                "SELECT province FROM localities GROUP BY province ORDER BY province ASC"
            )
            provinces = resp.fetchall()
            for province in provinces:
                create_csv_province(province[0])
            db.close()
    except Exception as e:
        print(f"Error al leer los datos: {e}")


def create_csv_province(province):
    db = get_db_instance()
    cur = db.cursor()
    with open(f"data_exports/{province}.csv", "w", newline="") as file:
        print(f"Creando csv de la provincia {province} con sus localidades.")
        try:
            writer = csv.writer(file)
            writer.writerow(["localidad", "cp", "id_prov_mstr"])
            if db:
                resp = cur.execute(
                    f"SELECT locality, postal_code, id_prov_mstr FROM localities WHERE province = '{province}' ORDER BY locality ASC"
                )
                data = resp.fetchall()
                writer.writerows(data)
                writer.writerow(
                    [f"{province} tiene un total de {len(data)} localidades"]
                )
                cur.close()
        except Exception as e:
            print(f"Error al leer los datos: {e}")
