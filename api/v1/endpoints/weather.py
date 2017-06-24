from flask_restplus import Resource
from api.v1.restplus import api_ns
import services.weather
import config.dev.http_codes as http_codes
import config.dev.urls as ext_api_urls

weather_ns = api_ns.namespace('smartmirror/weather', description='Operations related to weather')

@weather_ns.route('/current')
class CurrentWeather(Resource):
	@api_ns.response(200, http_codes._200)
	@api_ns.response(400, http_codes._400)
	@api_ns.response(503, http_codes._503)
	def get(self):
		"""
		Returns the current weather of the region as JSON on success.
		Uses openweathermap external API.
		Automatically determines location.
		"""
		response_dict = None
		code = 200

		location, status = services.geolocator.getLocation()
		if location is None:
			response_dict = {'status': http_codes._503, 'type': status.EXT_ERR, 'error_message': "Failed to make request to " + ext_api_urls.LOC_BASE}
			code = 503
			print(response_dict)
		else:
			lat = location['latitude']
			lon = location['longitude']

			weather, status = services.weather.getCurrentWeather(lat, lon)
			if weather is None:
				response_dict = {'status': http_codes._503, 'type': status.EXT_ERR, 'error_message': "Failed to make request to " + ext_api_urls.WTHR_BASE}
				code = 503
				print(response_dict)
			else:
				#print(weather)
				response_dict = {'status': http_codes._200, 'data':weather}
				#temp = weather['main']['temp']
				#cond = weather['weather'][0]['description']
			
		return response_dict, code
