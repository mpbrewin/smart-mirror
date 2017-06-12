########################
# Supported services for SmartMirror #
########################
import requests
import json

LOC_API = 'http://freegeoip.net/json'

# Returns the location of the pi as a lat, long pair
# else returns false and the status code
def getLocation():
	r = requests.get(LOC_API)
	if r.status_code == 200:
		j = json.loads(r.text)
		return j['latitude'], j['longitude']
	else:
		return False, r.status_code