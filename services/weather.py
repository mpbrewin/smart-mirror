import requests
import json
import config.dev.keys as api_keys
import config.dev.urls as ext_api_urls
import config.user_pref as user_config

# Generic http request to openweathermap
# endpoint refers to openweathermap's endpoint (which comes after the version number)
# e.g. api.openweathermap.org/data/2.5/endpoint?lat={lat}&lon={lon}
def httpOpenWeatherMap(endpoint, lat, lon):
	r = requests.get(ext_api_urls.WTHR_BASE + ext_api_urls.WTHR_VER + endpoint+ ext_api_urls.WTHR_PARAM_LAT + \
		str(lat) + '&' + ext_api_urls.WTHR_PARAM_LON + str(lon)  + '&' + ext_api_urls.WTHR_PARAM_UNIT + user_config.temp_units + '&' + \
		ext_api_urls.WTHR_PARAM_KEY + api_keys.WTHR_KEY )
	j = None

	if r.status_code == 200:
		j = json.loads(r.text)

	return j, r.status_code

# Returns the weather of the given lat and long as json
# else returns None and the status code
# API used: openweathermap
def getCurrentWeather(lat, lon):
	return httpOpenWeatherMap(ext_api_urls.WTHR_CURR, lat, lon)

# Returns a 5 day, 3 hour forecast of the give lat and lon as json
# else returns None and the status code
# API used: openweathermap
def getWeatherForecast(lat, lon):
	return httpOpenWeatherMap(ext_api_urls.WTHR_FCST, lat, lon)


