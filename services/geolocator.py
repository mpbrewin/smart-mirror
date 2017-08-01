import requests
import json

# URLs for ext api
LOC_BASE = 'http://freegeoip.net/json'

# Returns the location of the pi as a json object
# else returns None and the status code
# API used: freegeoip
# Schema: 
def getLocation():
	r = requests.get(LOC_BASE)
	loc = None
	
	if r.status_code == 200:
		loc = json.loads(r.text)

	return loc, r.status_code