from fit_db import get_db
from class_ejercicio import ejercicio


def insert_ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO fit (ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?, ?)"
    cursor.execute(statement, [ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad])
    db.commit()
    return True

def update_book(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE fit SET ejercicio = ?, repeticiones = ?, tiempo= ?, peso= ?, fortalece= ?, number_pages= ?, press= ? WHERE ID = ?"
    cursor.execute(statement, [ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad, ID])
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
    statement = "SELECT ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad FROM fit WHERE ID = ?"
    cursor.execute(statement, [ID])
    single_ejercicio = cursor.fetchone()
    ID = single_ejercicio[0]
    ejercicio = single_ejercicio[1]
    repeticiones = single_ejercicio[2]
    tiempo = single_ejercicio[3]
    peso = single_ejercicio[4]
    fortalece = single_ejercicio[5]
    serie = single_ejercicio[6]
    dificultad = single_ejercicio[7]
    ejercicio = ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)
    return ejercicio.serialize_details()


def get_ejercicio():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad FROM fit"
    cursor.execute(query)
    ejercicio_list = cursor.fetchall()
    list_of_ejercicios=[]
    for elem_ejercicio in ejercicio_list:
        ID = elem_ejercicio[0]
        ejercicio_nombre = elem_ejercicio[1]
        repeticiones = elem_ejercicio[2]
        tiempo = elem_ejercicio[3]
        peso = elem_ejercicio[4]
        fortalece = elem_ejercicio[5]
        serie = elem_ejercicio[6]
        dificultad = elem_ejercicio[7]
        ejercicio_to_add = ejercicio(ID, ejercicio_nombre, repeticiones, tiempo, peso, fortalece, serie, dificultad)
        list_of_ejercicios.append(ejercicio_to_add)
    return list_of_ejercicios 

flag = 0
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

