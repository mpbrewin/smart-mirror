# API bootstrap file - definitions of the RESTPlus API	  
from flask_restplus import Api
from flask import Flask, Blueprint

api = Api(version='1.0', title='SmartMirror API',
          description='Internal API for SmartMirror ')

api_blueprint = Blueprint('smartmirror/api/v1', __name__)
api.init_app(api_blueprint)

#Add each endpoint
#api.add_namespace(geolocator_namespace)
#api.add_namespace(weather_namespace)