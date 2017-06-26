/****Flags, constants, and configuration****/
var URL_BASE = "http://localhost:5000/smartmirror/api/v1/"
var LOC_API = URL_BASE + "geolocator"
var WTHR_API = URL_BASE + "weather/current"
var HOUR_FCST_API = URL_BASE + "weather/forecast/hourly" 
var WTHR_ICON_BASE ="http://openweathermap.org/img/w/"

var sc200 = "API_SUCCESS"

var CLK_INTERVAL = 1000 //1 sec
var WTHR_INTERVAL = 1800000 //30 min
var HOUR_FCST_INTERVAL = 3600000 //1 hr

var FORECAST_TABLE_WIDTH = 6

var MONTH_NAMES = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ] 
var DAY_NAMES= ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]



/****Globals****/
var lat = null
var lon = null
var state_code = null
var city = null



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
		state_code = response.data.region_code
		city = response.data.city
		city = city.replace(/ /g, "_") //replace all spaces with underscores
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

}

//Update hourly forecast
function updateHourlyForecast(){
	var fcst_path = HOUR_FCST_API
	if (state_code != null && city != null){
		fcst_path += "?state=" + state_code + "&city=" + city
	}

	$.get(fcst_path, function(response, status){
		console.log(response)
		for(var i=0; i<FORECAST_TABLE_WIDTH; i++){
			//Update the times
			var hourly_time = response.data.hourly_forecast[i*(24/FORECAST_TABLE_WIDTH)].FCTTIME.civil
			hourly_time = hourly_time.replace(":00", "") //Extract the hour number and period
			$('#hourly-time-' + i).html(hourly_time)
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
})