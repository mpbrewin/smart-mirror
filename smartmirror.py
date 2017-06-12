from flask import Flask
from views.display import display

app = Flask(__name__)

if __name__ == '__main__':
	app.register_blueprint(display, url_prefix='/smartmirror')
	app.run(debug=True, use_reloader=False)		# Start a development server in debug mode