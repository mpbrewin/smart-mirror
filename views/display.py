from flask import Blueprint, render_template
import services.geolocator
import services.weather
display = Blueprint('display', __name__)

@display.route('/')
def showDisplay():
	location, status = services.geolocator.getLocation()

	if location is None:
		print("Failed to retrieve location ", status)
	else:
		city = location['city']
		lat = location['latitude']
		lon = location['longitude']
		country = location['country_code']

		weather, status = services.weather.getCurrentWeather(lat, lon)
		if weather is None:
			print("Failed to retrieve weather ", status)
		else:
			print(weather)
			temp = weather['main']['temp']
			cond = weather['weather'][0]['description']

	return render_template('display.html')