from flask import Flask, jsonify, request
import json

tarefas = [
    {
        "id": 0,
        "responsavel":"maria",
        "tarefa": "desenvolver metodo GET",
        'status':  'pendente'
    },
    {
        "id": 1,
        "responsavel": "joao",
        "tarefa": "desenvolver metodo POST",
        'status': 'pendente'
    }

]
app = Flask(__name__)

@app.route('/tarefas/', methods=['POST', 'GET'])
def api_tarefas():
    if request.method=='POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id']= posicao
        tarefas.append(dados)
        return jsonify(dados)
    if request.method=='GET':
        return jsonify(tarefas)

@app.route('/tarefas/<int:id>', methods=['PUT', 'POST','GET', 'DELETE'])
def alterar_tarefas(id):
    if request.method=='PUT':
        dados = json.loads(request.data)
        tarefas[id]['status']= 'concluido'

        return jsonify(tarefas[id])
    elif request.method=='GET':
         dados = json.loads(request.data)

         return jsonify(dados)
    elif request.method == 'DELETE':
         dados =json.loads(request.data)

         tarefas.pop(id)
         return jsonify(tarefas)


if __name__ == '__main__':
    app.run(debug=True)


