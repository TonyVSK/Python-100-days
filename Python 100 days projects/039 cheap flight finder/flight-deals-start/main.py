#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


# STEP-BY-STEP

# 1 - Commit the file                                                   . OK
# 2 - find flight api                                                   . OK
# 3 - test sheety to populate the pending column                        .
# 4 - test communication with flight api                                . OK
# 5 - use flight information from the flight api to compare low prices  .
# 6 - if prices are lower, success                                      .
# 7 - test email api                                                    .
# 8 - activate email api when step 6 is satisfied                       .



# ======================================================================================================
from usefulkeys import flight_key
import requests
import json
from datetime import datetime


cities_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']

# API FLIGHT
def code_city(city):
    

    flight_endpoint = 'https://api.tequila.kiwi.com/locations/query'

    headers = {
        'apikey': flight_key
    }

    flight_params = {
        'term': city,
        #'location_types': 'city',
    }



    response = requests.get(url=flight_endpoint, headers=headers, params=flight_params)
    data = response.json()

    print(data['locations'][0]['code'])
    print(response)



for city in cities_list:
    code_city(city)