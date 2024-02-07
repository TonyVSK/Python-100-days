from apikey import api_key # you should create your own apikey.py file and create a variable api_key there, where you will provide your api key from openweather, format -> api_key = "yourAPIKeyHere"
import requests
import os
from twilio.rest import Client

    # WEATHER API
owm_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    'lat': 51.50,
    'lon': -0.127,
    'appid': api_key,
    'cnt': 4
}
response = requests.get(owm_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()




# ==========================================================================================
    # Twilio (SMS SENDER) API
from apikey import account_sid, auth_token, from_number, to_number

# At the Twilio API, we need these variables with that format:

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

# and the two numbers we will need; save it in environment variables for security, just like i did



# ==========================================================================================
    # Coding part

# print(type((weather_data['list'][0]['weather'][0]['id'])))
gonna_rain = False
for i in range (0, 4):
    weather_code = weather_data['list'][i]['weather'][0]['id']
    if weather_code <700:
        gonna_rain = True


if gonna_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Gonna rain today! take an umbrella",
                     from_=from_number,
                     to=to_number
                 )

else:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="That's ok, you can leave home today :)",
                     from_=from_number,
                     to=to_number
                 )
