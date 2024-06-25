from flask import Flask, jsonify, request
import ejercicio_controller_poo
from fit_db import create_tables

app = Flask(__name__)


@app.route('/ejercicio', methods=["GET"])
def get_ejercicio():
    ejercicios = ejercicio_controller_poo.get_ejercicio()
    ejercicios_list = []
    for ejercicio in ejercicios:
        elem = ejercicio.serialize()
        ejercicios_list.append(elem)
    return jsonify(ejercicios_list)

@app.route("/ejercicio/create", methods=["POST"])
def insert_ejercicio():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    repeticiones =ejercicio_details["repeticiones"]
    tiempo = ejercicio_details["tiempo"]
    peso = ejercicio_details["peso"]
    fortalece = ejercicio_details["fortalece"]
    serie = ejercicio_details["serie"]
    dificultad = ejercicio_details ["dificultad"]
    result = ejercicio_controller_poo.insert_ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)
    return jsonify(result)


@app.route("/ejercicio/gym/modify", methods=["PUT"])
def update_ejercicio_gym():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    dificultad = ejercicio_details["dificultad"]
    repeticiones =ejercicio_details["repeticiones"]
    series = ejercicio_details["series"]
    peso = ejercicio_details["peso"]
    result = ejercicio_controller_poo.update_ejercicio_gym(ID, ejercicio, dificultad, repeticiones, series, peso)
    return jsonify(result)
@app.route("/ejercicio/run/modify", methods=["PUT"])
def update_ejercicio_run():
    ejercicio_details = request.get_json()
    ID = ejercicio_details["ID"]
    ejercicio = ejercicio_details["ejercicio"]
    dificultad = ejercicio_details["dificultad"]
    distancia = ejercicio_details["distancia"]
    tiempo = ejercicio_details["tiempo"]
    result = ejercicio_controller_poo.update_ejercicio_gym(ID, ejercicio, dificultad, distancia, tiempo)
    return jsonify(result)

@app.route("/ejercicio/eliminate/<ID>", methods=["DELETE"])
def delete_ejercicio(ID):
    result = ejercicio_controller_poo.delete_ejercicio(ID)
    return jsonify(result)


@app.route("/ejercicio/<ID>", methods=["GET"])
def get_ejercicio_by_id(ID):
    ejercicio = ejercicio_controller_poo.get_by_id(ID)
    return jsonify(ejercicio)


if __name__ == '__main__':
    app.run()
