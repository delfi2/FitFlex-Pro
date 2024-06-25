from fit_db import get_db
from class_ejercicio import ejercicio


def insert_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, series, peso):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO fit_gym(ID, ejercicio, dificultad, repeticiones, series, peso) \
    VALUES ( ?, ?, ?, ? ,?, ?)"
    cursor.execute(statement, [ID, ejercicio, dificultad, repeticiones, series, peso])
    db.commit()
    return True
def insert_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO fit_run (ID, ejercicio, dificultad, distancia, tiempo) \
    VALUES ( ?, ?, ?, ? ,?)"
    cursor.execute(statement, [ID, ejercicio, dificultad, distancia, tiempo])
    db.commit()
    return True
def update_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, series, peso):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE fit_gym SET ejercicio = ?, dificultad = ?, repeticiones=, series=, peso= ? WHERE ID = ?"
    cursor.execute(statement, [ID, ejercicio, dificultad, repeticiones, series, peso])
    db.commit()
    return True
def update_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE fit_run SET ejercicio = ?, dificultad = ?, distancia = ?, tiempo = ? WHERE ID = ?"
    cursor.execute(statement, [ID, ejercicio, dificultad, distancia, tiempo])
    db.commit()
    return True

def delete_ejercicio(ID):
    db = get_db()
    cursor = db.cursor()
    ejercicio_eliminar = input("gym/run: ")
    if ejercicio_eliminar == "gym":
        statement = "DELETE FROM fit_gym WHERE ID = ?"
    elif ejercicio_eliminar == "run":
        statement = "DELETE FROM fit_run WHERE ID = ?"
    ID = (input("ID que del ejercicio que desea eliminar:  "))
    cursor.execute(statement, [ID])
    db.commit()
    return True


def get_by_id():
    db = get_db()
    cursor = db.cursor()
    ejercicio_buscar = input("gym/run: ")
    if ejercicio_buscar == "gym":
        statement = "SELECT ID, ejercicio, dificultad, repeticiones, series, peso FROM fit WHERE ID = ?"
    elif ejercicio_buscar == "run":
        statement = "SELECT ID, ejercicio, dificultad, distancia, tiempo FROM fit WHERE ID = ?"
    ID = input('Ingrese el ID buscado: ')
    cursor.execute(statement, [ID])
    return cursor.fetchone()


def get_ejercicio():
    db = get_db()
    cursor = db.cursor()
    ejercicio_buscar = input("gym/run")
    if ejercicio_buscar == "gym":
        query = "SELECT ID, ejercicio, dificultad, repeticiones, series, peso FROM fit_gym"
    elif ejercicio_buscar == "run":
        query = "SELECT ID, ejercicio, dificultad, distancia, tiempo FROM fit_run"
    cursor.execute(query)
    return cursor.fetchall()

def menu():
    print('******************Menu******************')
    print()
    print('ingrese 1 para agregar un ejercicio a la base de datos')
    print('ingrese 2 para eliminar un ejercicio de la base de datos')
    print('ingrese 3 para actualizar un ejercicio gym/run')
    print('ingrese 4 para listar todos los ejercicios segun su tipo')
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
            peso = input('ingrese el peso del ejercicio: ')
            series = int(input('ingrese el numero de series del ejercicio: '))
            result = insert_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, series, peso)
        elif tipo_ejercicio == "run":
            distancia = input('ingrese la distancia del ejercicio: ')
            tiempo = input('ingrese el tiempo que dura el ejercicio: ')
            result = insert_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo)
        if result == True:
            print('ejercicio ingresado correctamente')
            print()
            print()
        else:
            print('Error')
            print()

    elif opcion == 2:
        ID = int(input('ingrese el ID del ejercicio a eliminar: '))
        result = delete_ejercicio(ID)
        if result == True:
            print('ejercicio eliminado')
            print()
            print()
        else:
            print('Error')
            print()

    elif opcion == 3:
        tipo_ejercicio = input("Ingrese el tipo de ejercicio - gym/run")
        if tipo_ejercicio == "gym":
            update_ejercicio_gym
        elif tipo_ejercicio == "run":
            update_ejercicio_run

    elif opcion == 4:
        result = get_ejercicio()  # devuelve una lista de tuplas donde cada tupla es un registro
        print(result)
        print()
        print()

    elif opcion == 5:
        ID = int(input('ingrese el ID del ejercicio a buscar: '))
        result = get_by_id(ID)  # devuelve una tupla con el registro
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

