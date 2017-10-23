from flask import Blueprint, render_template

display = Blueprint('display', __name__)

@display.route('/')
def showDisplay():
	return render_template('display.html')
