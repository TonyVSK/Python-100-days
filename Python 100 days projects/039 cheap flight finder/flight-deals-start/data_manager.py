from usefulkeys import username, projectName, sheetName
import requests


class DataManager:
    def __init__(self, cities_code) -> None:
        self.sheety_endpoint = f'https://api.sheety.co/{username}/{projectName}/{sheetName}'
        self.sheety_params = {
            'username': username,
            'projectName': projectName,
            'sheetName': sheetName
        }
        self.response2 = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}')
        self.iD = 2
        self.cities_code = cities_code
        self.cities()


    def sheety_api(self, city, iD):
        prices = {
            'price': 
                {
                    "iataCode": city,
                }
            
        } 

        self.response3 = requests.put(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}/{iD}', json=prices)
        print(self.response3.text)
        self.response4 = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}?filter[familyFriendly]=true')
        print(self.response4.text)


    def cities(self):
        for city in self.cities_code:
            self.sheety_api(city, self.iD)
            self.iD += 1



