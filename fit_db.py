import sqlite3

DATABASE_NAME = "fit.db"


def get_db():  # devuelve un conector a la base de datos
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    table_gym = [
        """CREATE TABLE IF NOT EXISTS fit( 
                ID INTEGRER PRIMARY KEY,
                ejercicio TEXT NOT NULL,
                dificultad TEXT NOT NULL,
                repeticiones INTEGRER NOT NULL,
                serie INTEGRER NOT NULL, 
                peso TEXT NOT NULL             
            )
            """
    ]
    db = get_db()
    cursor = db.cursor() #permite ejecutar comandos
    table_run = [
        """CREATE TABLE IF NOT EXISTS fit( 
                ID INTEGRER PRIMARY KEY,
                ejercicio TEXT NOT NULL,
                dificultad TEXT NOT NULL,
                distancia TEXT NOT NULL,
                tiempo INTEGRER NOT NULL,       
            )
            """
    ]
    db = get_db()
    cursor = db.cursor() #permite ejecutar comandos
    
    for table in tables:
        cursor.execute(table)


def insert_ejercicio(ID, ejercicio, dificultad, repeticiones, series,
                     peso):  # atributos
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO fit (ID, ejercicio, dificultad, repeticiones, series,
                     peso) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?, ?)"
    cursor.execute(statement, [ID, ejercicio, dificultad, repeticiones, series,
                     peso])
    db.commit()
    return True


def delete_ejercicio(ID):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM fit WHERE ID = ?"
    cursor.execute(statement, [ID])
    db.commit()
    return True


def get_by_id(ID):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT ID, ejercicio, dificultad, repeticiones, series, peso FROM fit WHERE ID = ?"
    cursor.execute(statement, [ID])
    return cursor.fetchone()  # que me de un registro especifico


def get_ejercicios():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, ejercicio, dificultad, repeticiones, series, peso FROM fit"
    cursor.execute(query)
    return cursor.fetchall()  # me da todos los ejercicios





create_tables()
