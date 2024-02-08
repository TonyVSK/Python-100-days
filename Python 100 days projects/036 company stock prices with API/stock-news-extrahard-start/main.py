from apikey import key
import json

APIKEY = key
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# =======================================================================================================================================
# ## STEP 1: Use https://www.alphavantage.co
# # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

import requests

endpoint = 'https://www.alphavantage.co/query'
tesla_params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': STOCK,
    'interval': '60min',
    'apikey': APIKEY
}
r = requests.get(endpoint, params=tesla_params)
data = r.json()

my_dict = data["Time Series (60min)"]


lista = []
for item in my_dict:
    lista.append(item)



# DATE TO USE: THE LAST ONE
updated_stock = f"{lista[0]}"
# VALUE OF THE SHARE AT THIS DATE
value_of_share = float(my_dict[updated_stock]['1. open'])
print(f'Last Date: {updated_stock}')
print(f'Value of the stock: {value_of_share}')


print("\n\n")
# I NEED MY TODAY DATE AND YESTERDAY DATE TO MAKE AN COMPARATIVE
yesterday_stock = f"{lista[16]}"
yesterday_value_of_share = float(my_dict[yesterday_stock]['1. open'])
print(f'24 hours ago: {yesterday_stock}')
print(f'Value of the stock: {yesterday_value_of_share}')


comparating = value_of_share - yesterday_value_of_share
if comparating <0:
    if (comparating *(-1)) > (value_of_share/20):
        print('Bad news, the value decreased :C')

elif comparating > (yesterday_value_of_share/20):
    print('The value of the stock is bigger now')
else:
    print('No big flutuations')

# =======================================================================================================================================
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
from apikey import key2
APIKEY2 = key2

updated_stock = '2024-02-07'

endpoint2 = 'https://newsapi.org/v2/everything'
tesla_params2 = {
    'q' : 'Tesla',
    'from': updated_stock,
    'sortBy': 'popularity',
    'apiKey': APIKEY2

}
r2 = requests.get(endpoint2, params=tesla_params2)
data2 = r2.json()

my_dict2 = [data2['articles'][0]['title'], data2['articles'][1]['title'], data2['articles'][2]['title']]


print(my_dict2[0])
print(my_dict2[1])
print(my_dict2[2])

# =======================================================================================================================================
## STEP 3: Use email protocol module
# Send a seperate email with the percentage change and each article's title and description to your email. 
import smtplib
from apikey import email, passwordemail, email2

my_email = email
password = passwordemail
# # smtp-mail.outlook.com

if comparating <0:
    if (comparating *(-1)) > (value_of_share/20):
        with smtplib.SMTP(my_email, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=email2, 
                msg=f"Subject: Bad news, the value decreased :C\n\n{my_dict[0]}\n{my_dict[1]}\n{my_dict[2]}"
            )
        

elif comparating > (yesterday_value_of_share/20):

    with smtplib.SMTP(my_email, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email2, 
            msg=f"Subject: Good news: shares increased\n\n{my_dict[0]}\n{my_dict[1]}\n{my_dict[2]}"
        )

    
with smtplib.SMTP(my_email, port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=email2, 
        msg=f"Subject: It is the time!\n\nLook up, the ISS satellite is passing near you!"
    )