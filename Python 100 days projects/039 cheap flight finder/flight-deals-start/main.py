#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
"""
Unfortunately, the API had to be discontinued because the use of resources was limited and they were all used in testing the code.
Currently the code only obtains price values ​​for the specified dates, and saves the city codes in a spreadsheet on Google Sheets, 
in addition to sending an email notification through a third API to tell about lower values


"""


# =========================================================================================================================
# =========================================================================================================================
from usefulkeys import flight_key
import requests
import json
from datetime import datetime



# API FLIGHT
from flight_data import FlightData
flighting = FlightData
cities_code = flighting.cities_code

# =========================================================================================================================
# =========================================================================================================================
    # updating sheety API
from data_manager import DataManager
# I need to send cities_code
data = DataManager(cities_code)



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