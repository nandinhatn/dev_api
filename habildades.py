from flask_restful import Resource

habilidades = ['Python', 'Java', 'Flask', 'Django']

class Habilidades(Resource):
    def get(self):
        return habilidades
