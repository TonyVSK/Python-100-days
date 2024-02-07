from apikey import api_key # you should create your own apikey.py file and create a variable api_key there, where you will provide your api key from openweather, format -> api_key = "yourAPIKeyHere"
import requests

owm_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    'lat': 51.50,
    'lon': -0.127,
    'appid': api_key
}
response = requests.get(owm_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()
# If rain in the next 12 hours: 3, 6, 9 and 12 hours; the first 4 itens of the list
for i in range(0, 4):
    print(data["list"][i])
