from flask import Blueprint, render_template
import services
display = Blueprint('display', __name__)

@display.route('/')
def showDisplay():
	lat, lon = services.getLocation()
	if lat is False:
		print("Failed to retrieve location ", lon)
	else:
		print("Lat: ", lat, ", Lon: " lon)
    return render_template('display.html')