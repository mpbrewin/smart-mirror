from flask_restplus import Resource
from api.v1.restplus import api_ns
from api.v1.parsers import location_parser
import config.dev.http_codes as http_codes
import config.dev.urls as ext_api_urls
import services.weather

weather_ns = api_ns.namespace('weather', description='Operations related to weather')

@weather_ns.route('/current')
class CurrentWeather(Resource):
	@api_ns.expect(location_parser) #Location (as lat and lon) is optional
	@api_ns.response(200, http_codes._200)
	@api_ns.response(400, http_codes._400)
	@api_ns.response(503, http_codes._503)
	def get(self):
		"""
		Returns the current weather of the region as JSON.

		* Uses openweathermap external API.

		* API Key is hosted server side, and does not need to be provided.

		* The latitude and longitude can be provided as query parameters.

		* Example: 
		```
		smartmirror/weather/current?lat=34.1702&lon=-118.9558
		```

		* If lat and lon are not provided, the API will automatically determine the location of the PI by first calling ```smartmirror/geolocator```
		"""
		response_dict = None
		code = 200

		lat = None; lon = None
		location_args =  location_parser.parse_args()

		#parse location arguments (if present)
		if location_args['lat'] is None or location_args['lon'] is None:
			#lat and lon were not provided, determine location
			location, status = services.geolocator.getLocation()
			if location is None:	#Error
				response_dict = {'status': http_codes._503, 'type': http_codes.EXT_ERR, 'error_message': "Failed to make request to " + ext_api_urls.LOC_BASE}
				code = 503
				print(response_dict)
			else:
				lat = location['latitude']
				lon = location['longitude']
		else:
			#lat and lon were provided, parse them
			lat = location_args['lat']
			lon = location_args['lon']

		#weather
		weather, status = services.weather.getCurrentWeather(lat, lon)
		if weather is None:
			response_dict = {'status': http_codes._503, 'type': http_codes.EXT_ERR, 'error_message': "Failed to make request to " + ext_api_urls.WTHR_BASE}
			code = 503
			print(response_dict)
		else:
			response_dict = {'status': http_codes._200, 'data':weather}
			
		return response_dict, code

@weather_ns.route('/forecast')
class WeatherForecast(Resource):
	@api_ns.expect(location_parser) #Location (as lat and lon) is optional
	@api_ns.response(200, http_codes._200)
	@api_ns.response(400, http_codes._400)
	@api_ns.response(503, http_codes._503)
	def get(self):
		"""
		Returns the weather forecast of the region as JSON.

		* Uses openweathermap external API.

		* API Key is hosted server side, and does not need to be provided.

		* The forecast is over 5 days with data every 3 hours.

		* The latitude and longitude can be provided as query parameters.

		* Example: 
		```
		smartmirror/weather/forecast?lat=34.1702&lon=-118.9558
		```

		* If lat and lon are not provided, the API will automatically determine the location of the PI by first calling ```smartmirror/geolocator```
		"""
		response_dict = None
		code = 200

		lat = None; lon = None
		location_args =  location_parser.parse_args()

		#parse location arguments (if present)
		if location_args['lat'] is None or location_args['lon'] is None:
			#lat and lon were not provided, determine location
			location, status = services.geolocator.getLocation()
			if location is None:	#Error
				response_dict = {'status': http_codes._503, 'type': http_codes.EXT_ERR, 'error_message': "Failed to make request to " + ext_api_urls.LOC_BASE}
				code = 503
				print(response_dict)
			else:
				lat = location['latitude']
				lon = location['longitude']
		else:
			#lat and lon were provided, parse them
			lat = location_args['lat']
			lon = location_args['lon']

		#weather
		weather, status = services.weather.getWeatherForecast(lat, lon)
		if weather is None:
			response_dict = {'status': http_codes._503, 'type': http_codes.EXT_ERR, 'error_message': "Failed to make request to " + ext_api_urls.WTHR_BASE}
			code = 503
			print(response_dict)
		else:
			response_dict = {'status': http_codes._200, 'data':weather}
			
		return response_dict, code