from flask import Flask, jsonify, request
import ejercicio_controller_poo  # Importa el controlador
from apiter import get_lluvia
from fit_db import create_tables  # Importa la base de datos

app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Bienvenido a ~FitFlex_Pro~'
@app.route('/ejercicio', methods=["GET"])
def get_ejercicio():
    ejercicios = ejercicio_controller_poo.get_ejercicio()
    ejercicios_list = []
    for ejercicio in ejercicios:
        if len(ejercicio) == 6:  # Identifica si es un ejercicio de gym
            ej = ejercicio_controller_poo.ejercicio_gym(*ejercicio)
        else:  # Si no, es un ejercicio de running
            ej = ejercicio_controller_poo.ejercicio_run(*ejercicio)
        ejercicios_list.append(ej.serialize())
    return jsonify(ejercicios_list)

@app.route('/ejercicio/<int:ID>', methods=["GET"])
def get_ejercicio_by_id(ID):
    ejercicio = ejercicio_controller_poo.get_by_id(ID)
    if ejercicio:
        if len(ejercicio) == 6:  # Identifica si es un ejercicio de gym
            ej = ejercicio_controller_poo.ejercicio_gym(*ejercicio)
        else:  # Si no, es un ejercicio de running
            ej = ejercicio_controller_poo.ejercicio_run(*ejercicio)
        return jsonify(ej.serialize_detail())
    return jsonify({"error": "Ejercicio no encontrado"}), 404

@app.route("/ejercicio/gym/create", methods=["POST"])
def insert_ejercicio_gym():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    dificultad = ejercicio_details["dificultad"]
    repeticiones = ejercicio_details["repeticiones"]
    serie = ejercicio_details["serie"]
    peso = ejercicio_details["peso"]
    result = ejercicio_controller_poo.insert_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, serie, peso)
    return jsonify(result)

@app.route("/ejercicio/run/create", methods=["POST"])
def insert_ejercicio_run():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    dificultad = ejercicio_details["dificultad"]
    distancia = ejercicio_details["distancia"]
    tiempo = ejercicio_details["tiempo"]
    result = ejercicio_controller_poo.insert_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo)
    return jsonify(result)

@app.route("/ejercicio/gym/modify", methods=["PUT"])
def update_ejercicio_gym():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    dificultad = ejercicio_details["dificultad"]
    repeticiones = ejercicio_details["repeticiones"]
    serie = ejercicio_details["serie"]
    peso = ejercicio_details["peso"]
    result = ejercicio_controller_poo.update_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, serie, peso)
    return jsonify(result)

@app.route("/ejercicio/run/modify", methods=["PUT"])
def update_ejercicio_run():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    dificultad = ejercicio_details["dificultad"]
    distancia = ejercicio_details["distancia"]
    tiempo = ejercicio_details["tiempo"]
    result = ejercicio_controller_poo.update_ejercicio_run(ID, ejercicio, dificultad, distancia, tiempo)
    return jsonify(result)

@app.route("/ejercicio/eliminate/<int:ID>", methods=["DELETE"])
def delete_ejercicio(ID):
    result = ejercicio_controller_poo.delete_ejercicio(ID)
    return jsonify(result)
    
@app.route('/ejercicio/<int:ID>/lluvia', methods = ['GET'])
def get_run_lluvia(ID):
    elegir = get_ejercicio_by_id(ID)
    if elegir == []:
        return jsonify(status=400, description="Valor no valido para (" + ID + ")"), 400
    if ID != 0:
        lluvia = get_lluvia()
        result = lluvia
    return jsonify(result)
    
if __name__ == '__main__':
    create_tables()  # crea las tablas si no existen
    app.run()
