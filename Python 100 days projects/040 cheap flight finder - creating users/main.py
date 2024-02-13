from usefulkeys import username, projectName, sheetName, authorization, username2, projectName2, sheetName2
import requests



# # GET INFORMATION
# sheety_endpoint = f'https://api.sheety.co/{username}/{projectName}/{sheetName}'
# sheety_params = {
#     'username': username,
#     'projectName': projectName,
#     'sheetName': sheetName
# }
# response = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}')
# print(response.text)
# print(response.status_code)


## CREATING USER AT THE TABLE TO INSERT THEIR INFORMATIONS 
# POST USER INFORMATION

print('Welcome to the flight clube')
name= input('Please insert your first name: ')
lastName = input('Insert your last name: ')
email1 = 0
email2 = 1
while email1 != email2:
    email1 = input('Insert your email: ')
    email2 = input('Repeat again your email: ')
    if email1 != email2:
        print("The email don't match; please try again")

sheety_endpoint = f'https://api.sheety.co/{username2}/{projectName2}/{sheetName2}'
sheety_params = {
    'username': username2,
    'projectName': projectName2,
    'sheetName': sheetName2
}



headers = {
    "Authorization": f"Bearer {authorization}"
}

users = {
    'user': 
        {
            'name': name,
            'lastName': lastName,
            'email': email1
        }
    
} 



response = requests.post(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}', json=users, headers=headers)
print(response.text)
print(response.status_code)

# =======================================================================================================================================================
# =======================================================================================================================================================


# POST INFORMATIONS ABOUT FLIGHTS AND EMAIL ALERT
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import smtplib
from usefulkeys import my_email, password


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        with smtplib.SMTP(my_email, port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email, 
                        to_addrs=email1, 
                        msg=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
                    )