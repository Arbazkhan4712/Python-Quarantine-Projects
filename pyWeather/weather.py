#importing required modules
import requests, json

#enter your API key from openweathermap.org here
api_key = 'Your API key goes here'

#base url to store url from api
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#input city name here
city_name = input('Enter city name: ')

complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
response = requests.get(complete_url)
x = response.json()

#checking validity of city name
if x['cod'] != '404':
    y = x['main']
    current_temperature = y['temp']
    current_pressure = y['pressure']
    current_humidity = y['humidity']
    z = x['weather']
    weather_description = z[0]['description']
    q = x['wind']
    wind_speed = q['speed']
    wind_direction = q['deg']
    k = x['clouds']
    cloudliness = k['all']

    print('Temperature (in Kelvin) = ' + str(current_temperature) + '\n Atmospheric Pressure (in hPa) = ' + str(current_pressure) + '\n Humidity (in percentage) = ' + str(current_humidity) + '\n Wind Speed (in m/s) = ' + str(wind_speed) + '\n Wind Direction (in degrees) = ' + str(wind_direction) + '\n Cloudliness (in percentage) = ' + str(cloudliness) +  '\n Weather Description = ' + str(weather_description) )
else:
    print('City Not Found')
