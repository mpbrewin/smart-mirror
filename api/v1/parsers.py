#Parser modules to handle validation of the request paramaters
from flask_restplus import reqparse

current_weather_parser = reqparse.RequestParser()
current_weather_parser.add_argument('lat', type=float, required=False, location='args') #Location args refers to the query string in the url (after ?)
current_weather_parser.add_argument('lon', type=float, required=False, location='args')

hourly_forecast_parser = reqparse.RequestParser()
hourly_forecast_parser.add_argument('state', type=str, required=False, location='args')
hourly_forecast_parser.add_argument('city', type=str, required=False, location='args')
