#Parser modules to handle validation of the request paramaters
from flask_restplus import reqparse

location_parser = reqparse.RequestParser()
location_parser.add_argument('lat', type=float, required=False, location='args') #Location args refers to the query string in the url (after ?)
location_parser.add_argument('lon', type=float, required=False, location='args')
