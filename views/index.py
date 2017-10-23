from flask import Blueprint, redirect, url_for
from views.authorization import authorization
from views.display import display
index = Blueprint('index', __name__)

@index.route('/')
def routeIndex():
	return redirect(url_for('display.showDisplay'))
