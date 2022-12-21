from flask import Flask, request
from flask_restful import Resource, Api
from habildades import Habilidades #nome da class
import json
app = Flask(__name__)
api = Api(app)

desenvolvedores =[{
                    "id":0,
                    "nome": "Rafael",
                   "habilidades":["Python", "Flask"]},
                  {
                       "id":1,
                     "nome": "Maria",
                     "habilidades": ["Python", "Django"]
                  }]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor de ID {} não existe".format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido"
        return response

    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)

        return {'status':'sucesso', 'mensagem':'registro excluido'}
        pass

    def post(self):
        pass

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/')
api.add_resource(Habilidades,'/habilidades/')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
