import requests
from usefulkeys import flight_key


class FlightData:
    def __init__(self) -> None:
        self.cities_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
        self.cities_code = []
        self.cities_manager()


    # API FLIGHT
    def code_city(self, city):
        

        self.flight_endpoint = 'https://api.tequila.kiwi.com/locations/query'

        self.headers = {
            'apikey': flight_key
        }

        self.flight_params = {
            'term': city,
            #'location_types': 'city',
        }



        self.response = requests.get(url=self.flight_endpoint, headers=self.headers, params=self.flight_params)
        self.data = self.response.json()

        print(self.data['locations'][0]['code'])
        self.cities_code.append(self.data['locations'][0]['code'])


    def cities_manager(self):
        for city in self.cities_list:
            self.code_city(city)