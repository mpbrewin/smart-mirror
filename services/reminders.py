import json
from config.user_pref import reminders_service

def getReminders():
	reminders = []

	if reminders_service == 'iCal':
		from pyicloud import PyiCloudService
		iCloud = PyiCloudService()

		
		events = iCloud.calendar.events()
		for event in events:
			reminder ={}
			reminder['title'] = event['title']
			reminder['date'] = event['startDate'][1:6]
			reminders.append(reminder)

	elif reminders_service == 'Google':
		import os.path
		import httplib2
		from apiclient import discovery
		from oauth2client import client
		from oauth2client import tools
		from oauth2client.file import Storage
		import datetime

		## TAKEN DIRECTLY FROM GOOGLE'S EXAMPLE
		try:
			import argparse
			flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
		except ImportError:
			flags = None

		SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
		CLIENT_SECRET_FILE = 'google_cal_cred.json'
		APPLICATION_NAME = 'Smart Mirror'

		home_dir = os.path.expanduser('./config/auth/')
		print(home_dir)
		credential_dir = os.path.join(home_dir, 'credentials')
		if not os.path.exists(credential_dir):
			os.makedirs(credential_dir)
		credential_path = os.path.join(credential_dir,
				'google_cal_cred.json')

		store = Storage(credential_path)
		credentials = store.get()
		if not credentials or credentials.invalid:
			flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
			flow.user_agent = APPLICATION_NAME
			if flags:
				credentials = tools.run_flow(flow, store, flags)
			else: # Needed only for compatibility with Python 2.6
				credentials = tools.run(flow, store)
			print('Storing credentials to ' + credential_path)

		http = credentials.authorize(httplib2.Http())
		service = discovery.build('calendar', 'v3', http=http)

		now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
		events_result = service.events().list(
			calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
		events = events_result.get('items', [])
		## END

		for event in events:
			reminder ={}
			reminder['title'] = event['summary']

			# Format the date to match iCal format
			datetime_raw = event['start']['dateTime']
			datetime_info = datetime_raw.split('T') 	# full date, time
			date = datetime_info[0].split('-')	# year, month, day
			time_raw = datetime_info[1].split('-')	# time, something i dont know
			time =time_raw[0].split(':')		# hour, min, sec

			datetime_arr = []
			for d in date:
				datetime_arr.append(d)
			for t in time:
				datetime_arr.append(t)
			reminder['date'] = datetime_arr[0:5]

			reminders.append(reminder)

	return json.dumps(reminders)