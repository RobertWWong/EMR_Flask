# from flask.views import MethodView
from flask_restful import Resource

class SpecialtyAPI(Resource):

    def get(self):
        return f'Special world'

    def post(self):
        return 'This is a Special post'


class SpecialtiesAPI(Resource):

    def get(self, name):
        return f'Getting the {name} world'
    def put(self, name):
        return f'Updating the {name} world'

    def delete(self, name):
        return f'Removing the {name} world'
