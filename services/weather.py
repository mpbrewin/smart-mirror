import requests
import json
import config.auth.keys as api_keys
import config.user_pref as user_config

# URLs for external apis
OWM_BASE = 'http://api.openweathermap.org/data'
OWM_VER = '/2.5'
OWM_CURR = '/weather?'
OWM_FCST = '/forecast?'
OWM_PARAM_LAT='lat='
OWM_PARAM_LON='lon='
OWM_PARAM_KEY='APPID='
OWM_PARAM_UNIT='units='

WG_BASE = 'http://api.wunderground.com/api/'
WG_HOURLY = 'hourly'
WG_DAILY= 'forecast10day'


# Generic http request to openweathermap
# endpoint refers to openweathermap's endpoint / service (which comes after the version number)
# e.g. api.openweathermap.org/data/2.5/endpoint?lat={lat}&lon={lon}
def httpOpenWeatherMap(endpoint, lat, lon):
	r = requests.get(OWM_BASE + OWM_VER + endpoint+ OWM_PARAM_LAT + \
		str(lat) + '&' + OWM_PARAM_LON + str(lon)  + '&' + OWM_PARAM_UNIT + user_config.temp_units + '&' + \
		OWM_PARAM_KEY + api_keys.OPENWEATHERMAP_KEY )
	j = None

	if r.status_code == 200:
		j = json.loads(r.text)

	return j, r.status_code

# Generic http request to wunderground
# service refers to wunderground service (e.g. hourly forecast)
# http://api.wunderground.com/api/aac18a990202506d/hourly/q/CA/San_Fransisco.json
def httpWunderground(service, state, city):
	r = requests.get(WG_BASE + api_keys.WUNDERGROUND_KEY + "/" + service + "/q/" + state + "/" + city + ".json")
	j = None

	if r.status_code == 200:
		j = json.loads(r.text)

	return j, r.status_code

# Returns the weather of the given lat and long as json using openweathermap
# else returns None and the status code
# API used: openweathermap
def getCurrentWeather(lat, lon):
	return httpOpenWeatherMap(OWM_CURR, lat, lon)

# Uses wunderground api to determine hourly forecast for today
# wunderground uses state and city to locate weather conditions
def getHourlyForecast(state, city):
	return httpWunderground(WG_HOURLY, state, city)

# Returns a 5 day, 3 hour forecast of the give lat and lon as json
# else returns None and the status code
# API used: openweathermap
def getDailyForecast(lat, lon):
	return httpWunderground(WG_DAILY, lat, lon)


