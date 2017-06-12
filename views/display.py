from flask import Blueprint
display = Blueprint('display', __name__)

@display.route('/')
def hello_world():
    return 'Hello, Display!'