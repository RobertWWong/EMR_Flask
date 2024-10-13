from inits import app
from flask_restful import Api
from views import landing, specialty

# USE FLASK-RESTful, that was how we cut down on view_func passing
api = Api(app)

api.add_resource(landing.HelloAPI, '/hello')
api.add_resource(specialty.SpecialtyAPI, '/special')
api.add_resource(specialty.SpecialtiesAPI, '/special/<string:name>')

if __name__ == '__main__':
    app.run()
