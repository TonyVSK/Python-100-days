import requests
from datetime import datetime
import smtplib

# São Paulo center
MY_LAT = -23.550520
MY_LONG = -46.633308

# SUNSET AND SUNRISE DEFINITIONS
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG, 
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


# ISS DEFINITIONS
response2 = requests.get(url="http://api.open-notify.org/iss-now.json")
response2.raise_for_status()


data = response2.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])




# 3 steps:
# 1 and 2. If the ISS is close to current position And it is currently dark
if (longitude - MY_LONG <5 and longitude -MY_LONG >-5) and (latitude - MY_LAT <5 and latitude -MY_LAT >-5) and (time_now>18):
    pass 
    # 3. trigger email
