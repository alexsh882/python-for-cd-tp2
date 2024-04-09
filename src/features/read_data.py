import csv

def read_csv(file_path):
    try: 
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        return data
    except FileNotFoundError as e:
        print(f'No se encontró el archivo en la ubicación especificada: {e}')
        return None
