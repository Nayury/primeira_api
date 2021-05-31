from flask import Flask, jsonify, json, request

app = Flask(__name__)

@app.route('/<int:id>')
def pessoas(id):
    return jsonify({'id':id, 'nome': 'Rafael'})

# @app.route('/soma/<int:valor1>/<int:valor2>')
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2})

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})

if __name__ == '__main__':
    app.run(debug=True)
