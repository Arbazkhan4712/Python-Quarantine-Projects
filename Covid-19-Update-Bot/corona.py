import requests
import json
from win10toast import ToastNotifier
from time import sleep

r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

data = r.json()
text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'
		
while True:
	toast = ToastNotifier()
	toast.show_toast("Covid-19 Notification",text ,duration=20)
	sleep(60)
