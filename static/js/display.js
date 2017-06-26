/****Flags, constants, and configuration****/
var URL_BASE = "http://localhost:5000/smartmirror/api/v1/"
var LOC_API = URL_BASE + "geolocator"
var WTHR_API = URL_BASE + "weather/current"
var HOUR_FCST_API = URL_BASE + "weather/forecast/hourly"
var DAILY_FCST_API = URL_BASE + "weather/forecast/daily"

var WTHR_ICON_BASE = "https://icons.wxug.com/i/c/k/"

var sc200 = "API_SUCCESS"

var CLK_INTERVAL = 1000 //1 sec
var WTHR_INTERVAL = 1800000 //30 min
var HOUR_FCST_INTERVAL = 3600000 //1 hr
var DAILY_FCST_INTERVAL =43200000 //12 hrs

var FORECAST_TABLE_WIDTH = 6

var MONTH_NAMES = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ] 
var DAY_NAMES= ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

/*Since openweathermap has more accurate data, but wunderground has better icons,
  this map serves as a way to convert the openweathermap icon url to a wunderground
  icon url without a separate api call.
*/
var ICON_CONVERTER = [['01d', 'clear'], ['01n', 'nt_clear'], ['02d', 'partlycloudy'], ['02n', 'nt_partlycloudy'],
			['03d', 'mostlycloudy'], ['03n', 'nt_mostlycloudy'], ['04d', 'cloudy'], ['04n', 'nt_cloudy'],
			['09d', 'sleet'], ['09n', 'nt_sleet'], ['10d', 'rain'], ['10n', 'nt_rain'], ['11d', 'tstorms'],
			['11n', 'nt_tstorms'], ['13d', 'snow'], ['13n', 'nt_snow'], ['50d', 'fog'], ['50n', 'nt_fog']];
var ICON_MAP = new Map(ICON_CONVERTER)



/****Globals****/
var lat = null
var lon = null
var state_code = null
var city = null



/****Functions****/
//Capitalize the first letter of the word
function toCamelCase(word){
	return word.charAt(0).toUpperCase() + word.slice(1)
}

//Update the clock every second
function updateClock(){
	var date = new Date()
	date.setDate(date.getDate())

	var hour = date.getHours()
	var minute = date.getMinutes()
	var second = date.getSeconds()
	$('#time').html((hour > 12 ? hour - 12 : hour) + 
		":" + (minute < 10 ? "0" : "") + minute + 
		":" + (second < 10 ? "0" : "") + second)
	$('#period').html(hour < 12 ? "AM" : "PM")

	$('#dayofweek').html(DAY_NAMES[date.getDay()] + ", ")
	$('#month-day').html(MONTH_NAMES[date.getMonth()] + " " + date.getDate())	
}

//Get location as lat and lon. Called once upon page loading
function getLocation(){
	$.get(LOC_API, function(response, status){
		$('#city').html(response.data.city)
		lat = response.data.latitude
		lon = response.data.longitude
		state_code = response.data.region_code
		city = response.data.city
		city = city.replace(/ /g, "_") //replace all spaces with underscores
	})
}

//Update the current weather
function updateWeather(){
	var wthr_path = WTHR_API
	if (lat != null && lon != null){
		wthr_path += "?lat=" + lat + "&lon=" + lon
	}

	$.get(wthr_path, function(response, status){
		//Update the conditions
		var conditions = response.data.weather[0].description
		//CamelCase syntax to look nice
		var split_word = conditions.split(" ")
		var conditions_cc = ""
		for(var i=0; i<split_word.length; i++){
			conditions_cc += toCamelCase(split_word[i]) + " "
		}
		conditions_cc = conditions_cc.slice(0, -1);
		$('#conditions').html(conditions_cc)

		//Update the temperature
		$('#temperature').html(Math.round(response.data.main.temp) + "°")

		var icon_code = response.data.weather[0].icon
		var icon_url = WTHR_ICON_BASE + ICON_MAP.get(icon_code) + ".gif"
		$('#weather-icon').attr('src', icon_url)
	})
}


//Update hourly forecast
function updateHourlyForecast(){
	var fcst_path = HOUR_FCST_API
	if (state_code != null && city != null){
		fcst_path += "?state=" + state_code + "&city=" + city
	}

	$.get(fcst_path, function(response, status){
		for(var i=0; i<FORECAST_TABLE_WIDTH; i++){
			var idx_offset = i*(24/FORECAST_TABLE_WIDTH)

			//Update the times
			var hourly_time = response.data.hourly_forecast[idx_offset].FCTTIME.civil
			hourly_time = hourly_time.replace(":00", "") //Extract the hour number and period
			$('#hourly-time-' + i).html(hourly_time)

			//Update the temperatures
			var hourly_temp = response.data.hourly_forecast[idx_offset].feelslike.english
			$('#hourly-temp-' + i).html(hourly_temp +  "°")

			//Update the icons
			var hourly_icon_url = response.data.hourly_forecast[idx_offset].icon_url
			$('#hourly-icon-' + i).attr('src', hourly_icon_url)
		}
	})
}

//Update daily forecast
function updateDailyForecast(){
	var fcst_path = DAILY_FCST_API
	if (state_code != null && city != null){
		fcst_path += "?state=" + state_code + "&city=" + city
	}

	$.get(fcst_path, function(response, status){
		console.log(response)
		for(var i=0; i<FORECAST_TABLE_WIDTH; i++){ //0 corresponds to today. The first entry will be today's highs and lows
			//Update the days of the week
			if(i != 0){	//Leave the label of the first entry as today
				var dayofweek = response.data.forecast.txt_forecast.forecastday[i*2].title	//i*2 because odd entries are the night forecast for that day
				var abbrev = dayofweek.slice(0,3)
				$('#daily-dayofweek-' + i).html(abbrev)
			}
			
			//Update the highs
			var daily_high = response.data.forecast.simpleforecast.forecastday[i].high.fahrenheit
			$('#daily-high-' + i).html(daily_high + "°")

			//Update the lows
			var daily_low = response.data.forecast.simpleforecast.forecastday[i].low.fahrenheit
			$('#daily-low-' + i).html(daily_low + "°")

			//Update the icons
			var daily_icon_url = response.data.forecast.simpleforecast.forecastday[i].icon_url
			$('#daily-icon-' + i).attr('src', daily_icon_url)
		}
	})	
}

/****Main****/
$(document).ready(function(){
	setInterval(updateClock, CLK_INTERVAL)

	getLocation()

	updateWeather()
	setInterval(updateWeather, WTHR_INTERVAL)

	updateHourlyForecast()
	setInterval(updateHourlyForecast, HOUR_FCST_INTERVAL)

	updateDailyForecast()
	setInterval(updateDailyForecast, DAILY_FCST_INTERVAL)
})