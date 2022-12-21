from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class Desevolvedor(Resource):
    def get(self):
        return 'Ola dev'
#substitui a rota

api.add_resource(Desevolvedor,'/dev')

if __name__ == '__main__':
    app.run()
