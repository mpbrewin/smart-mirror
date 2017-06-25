/****Flags, constants, and configuration****/
var URL_BASE = "http://localhost:5000/smartmirror/api/v1/"
var LOC_API = URL_BASE + "geolocator"
var WTHR_API = URL_BASE + "weather/current"
var FCST_API = URL_BASE + "weather/forecast" 

var WTHR_ICON_BASE ="http://openweathermap.org/img/w/"

var sc200 = "API_SUCCESS"

var CLK_INTERVAL = 1000 //1 sec
var WTHR_INTERVAL = 1800000 //30 min
var FCST_INTERVAL = 86400000 //24 hr

var MONTH_NAMES = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ] 
var DAY_NAMES= ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

/****Globals****/
var lat = null
var lon = null

/****Functions****/
//Update the clock every second
function updateClock(){
	var date = new Date()
	date.setDate(date.getDate())

	var hour = date.getHours()
	var minute = date.getMinutes()
	var second = date.getSeconds()
	$('#time').html((hour > 12 ? hour - 12 : hour) + 
		":" + (minute < 10 ? "0" : "") + minute + 
		" " + (second < 10 ? "0" : "") + second)
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
	})
}

//Update the weather
function updateWeather(){
	var wthr_path = WTHR_API
	if (lat != null && lon != null){
		wthr_path += "?lat=" + lat + "&lon=" + lon
	}

	$.get(wthr_path, function(response, status){
		var icon_code = response.data.weather[0].icon
		var icon_url = WTHR_ICON_BASE + icon_code + ".png"
		$('#weather-icon').attr('src', icon_url)
		$('#temperature').html(Math.round(response.data.main.temp) + "°")
		$('#conditions').html(response.data.weather[0].description)
		//high = response.data.main.temp_max
		//low = response.data.main.temp_min
	})
}

//Update the forecast
function updateForecast(){
	var fcst_path = FCST_API
	if (lat != null && lon != null){
		fcst_path += "?lat=" + lat + "&lon=" + lon
	}

	$.get(fcst_path, function(response, status){
		console.log(response)
	})
}


/****Main****/
$(document).ready(function(){
	setInterval(updateClock, CLK_INTERVAL)
	getLocation()
	updateWeather()
	setInterval(updateWeather, WTHR_INTERVAL)
	updateForecast()
	setInterval(updateForecast, FCST_INTERVAL)
})