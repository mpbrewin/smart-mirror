$(document).ready(function(){
	var monthNames = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]; 
	var dayNames= ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];

	//Update the clock
	function updateClock(){
		var date = new Date();
		date.setDate(date.getDate());

		var hour = date.getHours();
		var minute = date.getMinutes();
		$('#time').html((hour > 12 ? hour - 12 : hour) + 
			":" + (minute < 10 ? "0" : "") + minute);
		$('#period').html(hour < 12 ? "AM" : "PM");

		$('#dayofweek').html(dayNames[date.getDay()] + ", ");
		$('#month-day').html(monthNames[date.getMonth()] + " " + date.getDate());	
	}
	setInterval(updateClock, 1000);

	//Update the weather
	function updateWeather(){

	}
});