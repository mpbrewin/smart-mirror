import requests
import json
import config.api.urls as api_urls

# Returns the location of the pi as a lat, long pair
# else returns false and the status code
def getLatAndLon():
	r = requests.get(api_urls.LOC_BASE)

	if r.status_code == 200:
		j = json.loads(r.text)
		return j['latitude'], j['longitude']
	else:
		return False, r.status_code