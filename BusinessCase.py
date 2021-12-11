from logging import debug
from flask import Flask, jsonify
from werkzeug.datastructures import *
from clases import Casos

app = Flask(__name__)

@app.route("/<string:_Id>")
def getVacante(_Id):
    VacanteEncontrada=[vacante for vacante in Casos if vacante["Id"] == _Id]
    if len(VacanteEncontrada) > 0:
        return jsonify({"Informacion": VacanteEncontrada[0]})
    return jsonify({"Mensaje": "Enlace no encontrado"})

@app.route("/<string:_Id>")
def getEmpresa(_Id):
    EmpresaHunty=[empresa for empresa in Casos if empresa["Id"] == _Id]
    if len(EmpresaHunty) > 0:
        return jsonify({"Empresa": EmpresaHunty[1]})
    return jsonify({"Mensaje": "Enlace no encontrado"})

if __name__ == "__main__":
    app.run (debug=True, port=4314)