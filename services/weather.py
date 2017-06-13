import requests
import json
from config.flags import temp_units
import config.api.keys as api_keys
import config.api.urls as api_urls

# Returns the weather of the given lat and long as json
# else returns false and the status code
# API used: openweathermap
def getCurrentWeather(lat, lon):
	r = requests.get(api_urls.WTHR_BASE + api_urls.WTHR_VER + api_urls.WTHR_CURR + api_urls.WTHR_PARAM_LAT + \
		str(lat) + '&' + api_urls.WTHR_PARAM_LON + str(lon)  + '&' + api_urls.WTHR_PARAM_UNIT + temp_units + '&' + \
		api_urls.WTHR_PARAM_KEY + api_keys.WTHR_KEY )

	if r.status_code == 200:
		j = json.loads(r.text)
		return j, r.status_code
	else:
		return None, r.status_code