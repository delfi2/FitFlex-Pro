from fit_db import get_db
from class_ejercicio import ejercicio_gym, ejercicio_run


def insert_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, serie, peso):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO fit_gym(ID, ejercicio, dificultad, repeticiones, serie, peso) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [ID, ejercicio, dificultad, repeticiones, serie, peso])
    db.commit()
    return True


def insert_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO fit_run (ID, ejercicio, dificultad, distancia, tiempo) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [ID, ejercicio, dificultad, distancia, tiempo])
    db.commit()
    return True


def update_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, serie, peso):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE fit_gym SET ejercicio = ?, dificultad = ?, repeticiones = ?, serie = ?, peso = ? WHERE ID = ?"
    cursor.execute(statement, [ejercicio, dificultad, repeticiones, serie, peso, ID])
    db.commit()
    return True


def update_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE fit_run SET ejercicio = ?, dificultad = ?, distancia = ?, tiempo = ? WHERE ID = ?"
    cursor.execute(statement, [ejercicio, dificultad, distancia, tiempo, ID])
    db.commit()
    return True


def delete_ejercicio(ID):
    db = get_db()
    cursor = db.cursor()
    statement_gym = "DELETE FROM fit_gym WHERE ID = ?"
    statement_run = "DELETE FROM fit_run WHERE ID = ?"
    cursor.execute(statement_gym, [ID])
    cursor.execute(statement_run, [ID])
    db.commit()
    return True


def get_by_id(ID):
    db = get_db()
    cursor = db.cursor()
    statement_gym = "SELECT ID, ejercicio, dificultad, repeticiones, serie, peso FROM fit_gym WHERE ID = ?"
    statement_run = "SELECT ID, ejercicio, dificultad, distancia, tiempo FROM fit_run WHERE ID = ?"
    cursor.execute(statement_gym, [ID])
    result = cursor.fetchone()
    if result:
        return result
    cursor.execute(statement_run, [ID])
    return cursor.fetchone()


def get_ejercicio():
    db = get_db()
    cursor = db.cursor()
    query_gym = "SELECT ID, ejercicio, dificultad, repeticiones, serie, peso FROM fit_gym"
    query_run = "SELECT ID, ejercicio, dificultad, distancia, tiempo FROM fit_run"
    cursor.execute(query_gym)
    result_gym = cursor.fetchall()
    cursor.execute(query_run)
    result_run = cursor.fetchall()
    return result_gym + result_run


def menu():
    print('******************Menu******************')
    print()
    print('ingrese 1 para agregar un ejercicio a la base de datos')
    print('ingrese 2 para eliminar un ejercicio de la base de datos')
    print('ingrese 3 para actualizar un ejercicio gym/run')
    print('ingrese 4 para listar todos los ejercicios')
    print('ingrese 5 para buscar un ejercicio por su ID')
    print('íngrese 6 para salir del menu')


flag = True
while flag:
    menu()

    opcion = int(input())

    if opcion == 1:
        ID = int(input('ingrese el ID del ejercicio: '))
        ejercicio = input('ingrese el ejercicio:')
        dificultad = input('ingrese la dificultad del ejercicio, - principiante; intermedio; avanzado - :')
        tipo_ejercicio = input("Ingrese el tipo de ejercicio - gym/run: ")
        if tipo_ejercicio == "gym":
            repeticiones = input('ingrese las repeticiones del ejercicio: ')
            peso = float(input('ingrese el peso del ejercicio en kg: '))
            serie = int(input('ingrese el numero de serie del ejercicio: '))
            result = insert_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, serie, peso)
        elif tipo_ejercicio == "run":
            distancia = float(input('ingrese la distancia del ejercicio en km: '))
            tiempo = float(input('ingrese el tiempo que dura el ejercicio en minutos: '))
            result = insert_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo)
        if result:
            print('ejercicio ingresado correctamente')
            print()
            print()
        else:
            print('Error')
            print()

    elif opcion == 2:
        ID = int(input('ingrese el ID del ejercicio a eliminar: '))
        result = delete_ejercicio(ID)
        if result:
            print('ejercicio eliminado')
            print()
            print()
        else:
            print('Error')
            print()

    elif opcion == 3:
        tipo_ejercicio = input("Ingrese el tipo de ejercicio - gym/run: ")
        if tipo_ejercicio == "gym":
            ID = int(input('ingrese el ID del ejercicio: '))
            ejercicio = input('ingrese el ejercicio:')
            dificultad = input('ingrese la dificultad del ejercicio, - principiante; intermedio; avanzado - :')
            repeticiones = input('ingrese las repeticiones del ejercicio: ')
            serie = int(input('ingrese el numero de serie del ejercicio: '))
            peso = input('ingrese el peso del ejercicio: ')
            result = update_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, serie, peso)
        elif tipo_ejercicio == "run":
            ID = int(input('ingrese el ID del ejercicio: '))
            ejercicio = input('ingrese el ejercicio:')
            dificultad = input('ingrese la dificultad del ejercicio, - principiante; intermedio; avanzado - :')
            distancia = input('ingrese la distancia del ejercicio: ')
            tiempo = input('ingrese el tiempo que dura el ejercicio: ')
            result = update_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo)
        if result:
            print('ejercicio actualizado correctamente')
            print()
            print()
        else:
            print('Error')
            print()

    elif opcion == 4:
        result = get_ejercicio()  # nos devuelve una lista de tuplas donde cada tupla es un registro
        print(result)
        print()
        print()

    elif opcion == 5:
        ID = int(input('ingrese el ID del ejercicio a buscar: '))
        result = get_by_id(ID)  # nos devuelve una tupla con el registro
        print(result)
        print()
        print()

    elif opcion == 6:
        print()
        print('saliendo')
        print()
        flag = False

print('terminado')
print('****************************************************')