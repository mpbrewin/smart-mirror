from flask import Blueprint, render_template, redirect, request
from services.spotify import authorizationURL as spotifyAuthorizationURL
from services.spotify import parseAuthorizationResponse as spotifyParseAuthorizationResponse
from services.spotify import requestAccessAndRefreshTokens as spotifyRequestTokens

authorization = Blueprint('authorization', __name__)

@authorization.route('/spotify')
def spotifyAuthorization():
	return redirect(spotifyAuthorizationURL()) #allow user to login to their account, granting access

# This is the url that the user is redirected to upon the user (not) permitting the application to get access
# to their account. The status of the authorization is embedded in the url.
# On success, the auth code will be used to request access and refresh tokens
# Otherwise, the error message is displayed
@authorization.route('/spotify/callback')
def spotifyAuthorizationCallback():
	success, auth_token =spotifyParseAuthorizationResponse()
	if success is True:
		#request refresh and access tokens
		tokens = spotifyRequestTokens(auth_token)

	else:
		render_template('spotify_access_denied.html', error=auth_token)	#auth_token will contain the error type