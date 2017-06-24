from flask_restplus import Resource
from api.v1.restplus import api_ns
import services.geolocator
import config.dev.http_codes as http_codes
import config.dev.urls as ext_api_urls

geolocator_ns = api_ns.namespace('smartmirror/geolocator', description='Operations related to geolocation')

@geolocator_ns.route('/')
class Geolocator(Resource):
	@api_ns.response(200, http_codes._200)
	@api_ns.response(400, http_codes._400)
	@api_ns.response(503, http_codes._503)
	def get(self):
		"""
		Returns the latitude and longitude of the pi as JSON on success.
		Uses freegeoip external API.
		"""
		response_dict = None
		code = 200

		location, status = services.geolocator.getLocation()
		if location is None:
			response_dict = {'status': http_codes._503, 'type': http_codes.EXT_ERR, 'error_message': "Failed to make request to " + ext_api_urls.LOC_BASE}
			code = 503
			print(response_dict)
		else:
			response_dict = {'status': http_codes._200, 'data': location}

		return response_dict, code
