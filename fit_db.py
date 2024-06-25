import sqlite3

DATABASE_NAME = "fit.db"


def get_db():  # devuelve un conector a la base de datos
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    table_gym = """
        CREATE TABLE IF NOT EXISTS fit_gym( 
                ID INTEGRER PRIMARY KEY,
                ejercicio TEXT NOT NULL,
                dificultad TEXT NOT NULL,
                repeticiones INTEGRER NOT NULL,
                series INTEGRER NOT NULL, 
                peso TEXT NOT NULL             
            )
        """
    db = get_db()
    cursor = db.cursor() #permite ejecutar comandos


    table_run = """CREATE TABLE IF NOT EXISTS fit_run( 
                ID INTEGRER PRIMARY KEY,
                ejercicio TEXT NOT NULL,
                dificultad TEXT NOT NULL,
                distancia TEXT NOT NULL,
                tiempo INTEGRER NOT NULL       
            )
        """
    db = get_db()
    cursor = db.cursor() #permite ejecutar comandos
    cursor.execute(table_gym)
    cursor.execute(table_run)

    db.commit()
    db.close()
create_tables()