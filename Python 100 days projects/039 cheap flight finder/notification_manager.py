import smtplib
import requests
from usefulkeys import username, projectName, sheetName, email, passwordemail, email2


class NotificationManager:
    def __init__(self, cities_values) -> None:
        self.cities_values = cities_values
        self.email2 = email2
        self.my_email = email
        self.password = passwordemail
        self.send_request()


    def send_request(self): 
        # I need the values of the sheets to compare 
        self.response_sheet = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}')
        self.sheet_data = self.response_sheet.json()

        # Saving prices at the sheets in a dict with the key of the city
        self.sheet_prices = {entry['IATACode']: entry['Lowest Price'] for entry in self.sheet_data['prices']}

        # key and value
        for city_code, price_list in self.cities_values.items():
            for price in price_list:
                
                if city_code in self.sheet_prices and price < self.sheet_prices[city_code]:
                    print(f'There is a lower value for {city_code}: {price} < {self.sheet_prices[city_code]}')
                    with smtplib.SMTP(self.my_email, port=587) as connection:
                        connection.starttls()
                        connection.login(user=self.my_email, password=self.password)
                        connection.sendmail(
                            from_addr=self.my_email, 
                            to_addrs=self.email2, 
                            msg=f"Subject: Good news! the value decreased to flight\n\nThere is a lower value for {city_code}: {price} < {self.sheet_prices[city_code]}"
                        )


