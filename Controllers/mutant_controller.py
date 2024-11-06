from flask import Flask,jsonify, request
from Services.detect_mutant import is_mutant, detect_and_save
from repositories.mutant_repository import MutantRepository
from model import db  # Asegúrate de importar db
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

# Configura la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://base_de_mutantes_user:LgA2ruxr3UYXfMxRLPz1nOcFNAkrVhNm@dpg-cskpn2rv2p9s73a9i6f0-a.oregon-postgres.render.com/base_de_mutantes'  # Variable de entorno
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def root():
    return "root"

@app.route("/mutantes")
def get_mutantes():
    mutantes = MutantRepository.get_all()
    return jsonify(mutantes)

@app.route("/stats")
def get_stats():
    mutantes = MutantRepository.get_stats()
    return jsonify([mutant.to_dict() for mutant in mutantes])



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
        result = detect_and_save(dna_values)
    
    if result:
        return jsonify({"Resultado": "Es un mutante"}), 200
    else:
        return jsonify({"Resultado":"No es un mutante."}),403






if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    app.run(debug=True,host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))