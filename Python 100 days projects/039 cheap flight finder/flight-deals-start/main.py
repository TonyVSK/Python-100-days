#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


# STEP-BY-STEP

# 1 - commit the file                                                   . OK
# 2 - find flight api                                                   . OK
# 3 - test sheety to populate the pending column                        . OK
# 4 - test communication with flight api                                . OK
# 5 - use flight information from the flight api to compare low prices  . OK
# 6 - if prices are lower, success                                      .
# 7 - test email api                                                    .
# 8 - activate email api when step 6 is satisfied                       .
# 9 - make an organization in classes                                   .


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
    response4 = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}')
    print(response4.text)


iD = 2
for city in cities_code:
    sheety_api(city, iD)
    iD += 1




# =========================================================================================================================
# =========================================================================================================================

from usefulkeys import key2

search_endpoint2 = 'https://api.tequila.kiwi.com/v2/search'
headers = {'apikey': key2}
    
search_params = {
    'fly_from': 'SAO',
    'fly_to': 'PRG',
    'date_to': '03/08/2024',
}

response2 = requests.get(url=search_endpoint2, headers=headers, params=search_params)
data2 = response2.json()

for flight in data2['data']:
    print(f"Preço: {flight['price']}, Companhia aérea: {flight['airlines'][0]}, Data de partida: {flight['local_departure'][:10]}")