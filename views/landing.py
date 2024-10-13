from flask import request
from flask_restful import Resource

class HelloAPI(Resource):

    def get(self):
        if request.args:
            print('Parameters have been given')
            for k, v in request.args.items():
                print(f'{k} = {v}')

        return 'Hello world, this endpoints accepts parameters'

    def post(self):
        return 'This is a post'
