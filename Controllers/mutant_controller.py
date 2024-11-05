from flask import Flask,jsonify, request

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
def check_dna(mutante_id):
    data = request.get_json()
    return jsonify(data), 201







if __name__ == '__main__':
    app.run(debug=True)