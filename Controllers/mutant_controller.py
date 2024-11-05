from flask import Flask,jsonify, request
# from Services.detect_mutant import is_mutant
# import sys
import os

# # Agregar la ruta del directorio que contiene Services al PYTHONPATH
# # Esto se hace asumiendo que este script está en Controllers
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Services')))

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

@app.route("/mutant", methods=['POST'])
def check_dna():
    data = request.get_json()
    result = is_mutant(data)
    return jsonify(result), 201







if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))