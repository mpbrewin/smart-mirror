from flask_restplus import Resource
from api.v1.restplus import api_ns
from api.v1.parsers import location_parser
import config.dev.http_codes as http_codes
import config.dev.urls as ext_api_urls
import services.weather

weather_ns = api_ns.namespace('smartmirror/weather', description='Operations related to weather')

@weather_ns.route('/current')
class CurrentWeather(Resource):
	@api_ns.expect(location_parser) #Location (as lat and lon) is optional
	@api_ns.response(200, http_codes._200)
	@api_ns.response(400, http_codes._400)
	@api_ns.response(503, http_codes._503)
	def get(self):
		"""
		Returns the current weather of the region as JSON.

		Uses openweathermap external API.

		The latitude and longitude can be provided as a query.

		Example: 
		```
		smartmirror/weather/current?lat=34.1702&lon=-118.9558
		```

		If lat and lon is not provided, the API will automatically determine the location of the PI by first calling ```smartmirror/geolocator```
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

