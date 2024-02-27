from bs4 import BeautifulSoup
import requests

# ===================================================================================================================================
# SCRAPING AMAZON PROCUCT PAGE TO GET PRICE
URL = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

# GETTING HOUSEs ADDRRESS   
house_links = soup.find_all(name="a", class_='StyledPropertyCardDataArea-anchor')
house_links = [house.getText().strip() for house in house_links]
print(house_links)


# GETTING HOUSE PRICES
house_prices = soup.find_all(class_='PropertyCardWrapper')
house_prices = [house.getText().strip() for house in house_prices]
print(house_prices)


# GETTING HOUSEs LINK
house_links = soup.find_all(name="a", class_='StyledPropertyCardDataArea-anchor')
house_links = [house.get('href').strip() for house in house_links]
print(house_links)