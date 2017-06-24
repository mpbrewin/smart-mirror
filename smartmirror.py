from flask import Flask
from api.v1.restplus import api_blueprint
from views.display import display

app = Flask(__name__)

if __name__ == '__main__':
	#Register display page
	app.register_blueprint(display, url_prefix='/smartmirror')

	#Register api namespace
	app.register_blueprint(api_blueprint, url_prefix="/smartmirror/api/v1")

	app.run(debug=True, use_reloader=False)		# Start a development server in debug mode