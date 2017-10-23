from flask_restplus import Resource
from api.v1.restplus import api_ns
import api.v1.http_codes as http_codes
import services.spotify

spotify_ns = api_ns.namespace('spotify', description='Operations related to spotify')

# @spotify_ns.route('/authorize')
# class AuthorizationRequest(Resource):
# 	@api_ns.response(200, http_codes._200)
# 	@api_ns.response(400, http_codes._400)
# 	@api_ns.response(503, http_codes._503)
# 	def get(self):
# 		"""
# 		Requests spotify user authorization 
# 		"""
# 		response_dict = None
# 		stuff, code = services.spotify.authorize()

# 		return response_dict, code

@spotify_ns.route('/new-releases')
class NewReleasesRequest(Resource):
	@api_ns.response(200, http_codes._200)
	@api_ns.response(400, http_codes._400)
	@api_ns.response(503, http_codes._503)
	def get(self):
		"""
		Requests new releases of artists the user follows or frequents
		"""
		response_dict = None
		
		return response_dict, code