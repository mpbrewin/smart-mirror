import requests
import json
import config.dev.urls as api_urls

# Returns the location of the pi as a json object
# else returns false and the status code
# API used: freegeoip
# Schema: 
def getLocation():
	r = requests.get(api_urls.LOC_BASE)
	loc = None
	
	if r.status_code == 200:
		loc = json.loads(r.text)

	return loc, r.status_code