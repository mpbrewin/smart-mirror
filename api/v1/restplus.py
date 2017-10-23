# API bootstrap file - definitions of the RESTPlus API	  
from flask_restplus import Api
from flask import Flask, Blueprint

api_ns = Api(version='1.0', title='SmartMirror API', description='Internal API for SmartMirror ')
api_blueprint = Blueprint('smartmirror/api/v1', __name__)
api_ns.init_app(api_blueprint)


#Add each endpoint
from api.v1.endpoints.geolocator import geolocator_ns
from api.v1.endpoints.weather import weather_ns
from api.v1.endpoints.reminders import reminders_ns
from api.v1.endpoints.spotify import spotify_ns

api_ns.add_namespace(geolocator_ns)
api_ns.add_namespace(weather_ns)
api_ns.add_namespace(reminders_ns)
api_ns.add_namespace(spotify_ns)