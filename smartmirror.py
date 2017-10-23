from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.v1.restplus import api_blueprint
from views.index import index
from views.display import display
from views.authorization import authorization

app = Flask(__name__)

if __name__ == '__main__':
	#Register api namespace
	app.register_blueprint(api_blueprint, url_prefix="/smartmirror/api/v1")

	#Register authorization namespace
	app.register_blueprint(authorization, url_prefix='/smartmirror/authorization')

	#Register display page
	app.register_blueprint(display, url_prefix='/smartmirror/display')

	#Register index page
	app.register_blueprint(index, url_prefix='/smartmirror')

	app.run(debug=True, use_reloader=False)		# Start a development server in debug mode