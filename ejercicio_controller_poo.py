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
        statement = "DELETE FROM ejercicio_gym WHERE ID = ?"
    elif ejercicio_eliminar == "run":
        statement = "DELETE FROM ejercicio_run WHERE ID = ?"
    ID = (input("ID que del ejercicio que desea eliminar:  "))
    cursor.execute(statement, [ID])
    db.commit()
    return True


def get_by_id():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad FROM fit WHERE ID = ?"
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
    print('ingrese 3 para buscar un ejercicio por su ID')
    print('ingrese 4 para listar todos los ejercicios')
    print('íngrese 5 para salir del menu')

flag = True
while flag:
    menu()

    opcion = int(input())

    if opcion == 1:
        ID = int(input('ingrese el ID del ejercicio: '))
        ejercicio = input('ingrese el ejercicio:')
        repeticiones = input('ingrese las repeticiones del ejercicio: ')
        peso = int(input('ingrese el peso del ejercicio: '))
        serie = int(input('ingrese el numero de serie del ejercicio: '))
        dificultad = input('ingrese la dificultad del ejercicio, - principiante; intermedio; avanzado - :')
        result = insert_ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)
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
        ID = int(input('ingrese el ID del ejercicio a buscar: '))
        result = get_by_id(ID)  # devuelve una tupla con el registro
        print(result)
        print()
        print()

    elif opcion == 4:
        result = get_ejercicios()  # devuelve una lista de tuplas donde cada tupla es un registro
        print(result)
        print()
        print()

    elif opcion == 5:
        print()
        print('saliendo')
        print()
        flag = False

print('terminado')
print('****************************************************')

