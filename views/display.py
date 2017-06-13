from flask import Blueprint, render_template
import services.geolocator
import services.weather
display = Blueprint('display', __name__)

@display.route('/')
def showDisplay():
	lat, lon = services.geolocator.getLatAndLon()

	if lat is False:
		print("Failed to retrieve location ", lon)
	else:
		print("Lat: ", lat, ", Lon: ", lon)
		weather, status = services.weather.getCurrentWeather(lat, lon)
		if weather is False:
			print("Failed to retrieve weather ", status)
		else:
			print(weather)

	return render_template('display.html')