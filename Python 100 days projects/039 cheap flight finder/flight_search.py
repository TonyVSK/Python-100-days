from usefulkeys import key2
import requests



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, cities_code) -> None:
        self.cities_code = cities_code
        self.key2 = key2
        self.pricing()






    def getting_price(self, city_code):
        

        search_endpoint2 = 'https://api.tequila.kiwi.com/v2/search'
        headers = {'apikey': self.key2}
            
        search_params = {
            'fly_from': 'LON',
            'fly_to': city_code,
            'date_to': '03/08/2024',
        }

        response2 = requests.get(url=search_endpoint2, headers=headers, params=search_params)
        data2 = response2.json()


        pricing = []
        dating = []

        for flight in data2['data']:
            price = int(flight['price'])
            date = flight['local_departure'][:10]
            pricing.append(price)
            dating.append(date)
        
        return pricing, dating







    def pricing(self):
        prices = []
        dates = []

        for i in range(0, len(self.cities_code)):
            prices2, dates2 = self.getting_price(self.cities_code[i])
            prices.append(prices2)
            dates.append(dates2)


        self.cities_values = { }


        self.cities_values = {city_code: [] for city_code in self.cities_code}

        for i in range(len(self.cities_code)):

            for price in prices[i]:
                self.cities_values[self.cities_code[i]].append(price)


        for city_code, price_list in self.cities_values.items():
            print(f'{city_code}: {price_list}')



            # I need to get self.cities_values at this class