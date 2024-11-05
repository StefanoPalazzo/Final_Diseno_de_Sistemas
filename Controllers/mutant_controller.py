from flask import Flask,jsonify, request
from Services.detect_mutant import is_mutant
# import sys
import os



app = Flask(__name__)

@app.route("/")
def root():
    return "root"

@app.route("/mutantes")
def get_mutantes():
    return "mutantes"

    return "root"

@app.route("/mutantes/<mutante_id>")
def get_mutante_id(mutante_id):
    mutante = {"id": mutante_id, "name": "pedro"}
    return jsonify()

@app.route("/mutant", methods=['POST'])
def check_dna():
    data = request.get_json()
    if not data or 'dna' not in data:
        return jsonify({"error": "Solicitud mal formada: se esperaba un objeto JSON con la clave 'dna'."}), 400

    if "dna" in data.keys():
        dna_values = data["dna"]
        result = is_mutant(dna_values)
    
    if result:
        return jsonify({"Resultado": "Es un mutante"}), 201
    else:
        return jsonify({"Resultado":"No es un mutante."}),1






if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))