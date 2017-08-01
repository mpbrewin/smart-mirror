from flask_restplus import Resource
from api.v1.restplus import api_ns
import api.v1.http_codes as http_codes
import services.reminders

reminders_ns = api_ns.namespace('reminders', description='Operations related to the reminders list')

@reminders_ns.route('/')
class Reminders(Resource):
	@api_ns.response(200, http_codes._200)
	@api_ns.response(400, http_codes._400)
	@api_ns.response(503, http_codes._503)
	def get(self):
		"""
		Returns the list of events as JSON.
		The title of the event and its date and time are part of the JSON
		"""
		response_dict = None
		code = 200

		reminders_list = services.reminders.getReminders()
		response_dict = {'status': http_codes._200, 'data': reminders_list}

		return response_dict, code
