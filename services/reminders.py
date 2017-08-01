import json
from config.user_pref import reminders_service

def getReminders():
	if reminders_service == 'iCal':
		from pyicloud import PyiCloudService
		iCloud = PyiCloudService()

		reminders = []
		events = iCloud.calendar.events()
		for event in events:
			reminder ={}
			reminder['title'] = event['title']
			reminder['date'] = event['startDate'][1:6]
			reminders.append(reminder)

		return json.dumps(reminders)
	elif reminders_service == "Google_Calendar":
		
	
