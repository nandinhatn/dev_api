from flask import Flask , jsonify, request
import json




desenvolvedores =[{
                    'id':'0',
                    'nome': 'Rafael',
                   'habilidades':['Python', 'Flask']},
                  {
                       'id':1,
                     'nome': 'Maria',
                      'habilidades': ['Python', 'Django']
                  }]

app = Flask(__name__)

@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor de ID {} não existe".format(id)
            response= {'status':'erro','mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido"
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id]= dados
        return jsonify(dados)
    elif request.method =='DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'registro excluido'})
@app.route('/dev/', methods= ['GET', 'POST'])
def lista_desenvolvedores():
    if request.method =='POST':
        dados= json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id']= posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method=='GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)