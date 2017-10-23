import requests
import json
import base64
from config.auth.credentials.spotify_cred import CLIENT_ID as client_id
from config.auth.credentials.spotify_cred import CLIENT_SECRET as client_secret

# URLs for external API
# endpoints
BASE = 'https://accounts.spotify.com/'
AUTHORIZE = 'authorize/?'
API = 'api/'
TOKEN= 'token'
# params for GET
PARAM_CLIENT = 'client_id='
PARAM_RESPONSE = 'response_type='
PARAM_REDIRECT = 'redirect_uri='
PARAM_STATE = 'state='
PARAM_SCOPE = 'scope='
# keys for POST
KEY_GRANT= 'grant_type'
KEY_CODE = 'code'
KEY_REDIRECT = 'redirect_uri'
KEY_AUTH ='Authorization'

callback_url = 'http://localhost:5000/smartmirror/authorization/spotify/callback'
scopes = 'user-top-read%20user-follow-read'	#top artists of user, and artists they actively follow


## AUTHORIZATION ##
# Hard coded url for spotify authorization
def authorizationURL():
	spotifyURL = BASE + AUTHORIZE + PARAM_CLIENT + client_id + '&' + PARAM_RESPONSE + 'code' + \
		'&' + PARAM_REDIRECT + callback_url + '&' + PARAM_SCOPE + scopes

	return spotifyURL

# The status of the authorization, along with the authorization code, are embedded in the url on success
# These values are returned (code as string)
# Otherwise, the error message is returned
def parseAuthorizationResponse():
	auth_code = request.args.get('code')
	error = request.args.get('error')
	# Assume the worst, failure
	success = False
	res = error

	if error is None:
		success = True
		res = str(auth_code)

	return success, res

# The authorization code is used to request access and refresh tokens via a POST request
# POST body must contain grant_type, auth_code, and the redirect_uri (even though no redirection occurs, just for validation purposes)
# Request header must contain an Authorization parameter set to the base 64 encoded string containing the clientID and secret key.
# format: Authorization: Basic <base64 encoded client_id:client_secret>
#
# If successful, this function will return both the response body containing the access token, token type, scope, expiration offset, and refresh token
# Returns none on failure
def requestAccessAndRefreshTokens(auth_code):
	post_payload = {
		KEY_GRANT : 'authorization_code',
		KEY_CODE : auth_code,
		KEY_REDIRECT : callback_url
	}
	encoded_id_secret = base64.b64encode("{}:{}".format(client_id, client_secret))
	headers = {KEY_AUTH : "Basic {}".format(encoded_id_secret)}

	response = requests.post(BASE + API + TOKEN, data=post_payload, headers=headers)
	j = None

	if response.status_code == 200:
		j = json.loads(response.text)

	return j


## RETRIEVAL ##

def getNewReleases():
	

