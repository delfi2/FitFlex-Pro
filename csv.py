import sqlite3
import csv


def export_to_csv(fit_db, ejercicio_gym, gym):
    # Nos conectamos a la base de datos
    conn = sqlite3.connect(fit_db)
    cursor = conn.cursor()

    # Ejecutamos una consulta para seleccionar todos los datos de la tabla
    cursor.execute(f"SELECT * FROM {ejercicio_gym}")

    # Obtenemos los nombres de las columnas
    column_names = [description[0] for description in cursor.description]

    # Abrir el archivo CSV en modo escritura
    with open(gym, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Escribimos los nombres de las columnas en el archivo CSV
        writer.writerow(column_names)

        # Escribimos los datos de la tabla en el archivo CSV
        for row in cursor.fetchall():
            writer.writerow(row)

    # Cerramos la conexión a la base de datos
    conn.close()


# Exportar la tabla 'fit_gym' a 'fit_gym.csv'
export_to_csv('fit.db', 'fit_gym', 'fit_gym.csv')

# Exportar la tabla 'fit_run' a 'fit_run.csv'
export_to_csv('fit.db', 'fit_run', 'fit_run.csv')


def reader(csv_file):
    return None
