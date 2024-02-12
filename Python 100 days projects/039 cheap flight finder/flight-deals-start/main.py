#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
"""
Unfortunately, the API had to be discontinued because the use of resources was limited and they were all used in testing the code.
Currently the code only obtains price values ​​for the specified dates, and saves the city codes in a spreadsheet on Google Sheets, 
in addition to sending an email notification through a third API
"""


# =========================================================================================================================
# =========================================================================================================================
from usefulkeys import flight_key
import requests
import json
from datetime import datetime


cities_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
cities_code = []
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
    cities_code.append(data['locations'][0]['code'])



for city in cities_list:
    code_city(city)

# =========================================================================================================================
# =========================================================================================================================
from usefulkeys import username, projectName, sheetName
sheety_endpoint = f'https://api.sheety.co/{username}/{projectName}/{sheetName}'
sheety_params = {
    'username': username,
    'projectName': projectName,
    'sheetName': sheetName
}

response2 = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}')
print(response2.text)


# POST REQUEST
# from usefulkeys import authorization
# headers = {
#     "Authorization": f"Bearer {authorization}"
# }


def sheety_api(city, iD):
    prices = {
        'price': 
            {
                "iataCode": city,
            }
        
    } 

    response3 = requests.put(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}/{iD}', json=prices)
    print(response3.text)
    response4 = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}?filter[familyFriendly]=true')
    print(response4.text)


iD = 2
for city in cities_code:
    sheety_api(city, iD)
    iD += 1




# =========================================================================================================================
# =========================================================================================================================
    # Getting the cities_values
from flight_search import FlightSearch

flight = FlightSearch(cities_code)
cities_values = flight.cities_values
# I need to get self.cities_values at this class
# =========================================================================================================================
# =========================================================================================================================
    # convert to class sending cities_values
from notification_manager import NotificationManager

NotificationManager(cities_values)