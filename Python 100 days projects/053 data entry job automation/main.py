from bs4 import BeautifulSoup
import requests

# ===================================================================================================================================
# SCRAPING ZULLOW CLONE TO GET ALL DATA TO FILL THE FORM
URL = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

# GETTING HOUSEs ADDRRESS   
house_address = soup.find_all(name="a", class_='StyledPropertyCardDataArea-anchor')
house_address = [house.getText().strip() for house in house_address]
print(house_address)


# GETTING HOUSE PRICES
house_prices = soup.find_all(class_='PropertyCardWrapper')
house_prices = [house.getText().strip() for house in house_prices]
print(house_prices)


# GETTING HOUSEs LINK
house_links = soup.find_all(name="a", class_='StyledPropertyCardDataArea-anchor')
house_links = [house.get('href').strip() for house in house_links]
print(house_links)



# ===================================================================================================================================
# FILLING FORM WITH THE DATA USING SELENIUM

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


URL = 'https://docs.google.com/USEYOURDOCSLINKHERE'

# Keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option) # we will work with chrome



for i in range(0, len(house_address)):
    driver.get(URL)
    # ADDRESS INPUT
    sleep(2)
    address_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(house_address[i], Keys.TAB)
    # PRICE INPUT
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(house_prices[i], Keys.TAB)
    # LINK INPUT
    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(house_links[i])

    # SEND BUTTON
    send_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send_button.click()
    sleep(2)


    # DON'T FORGET TO GENERATE THE SHEETS IN OPTIONS OF YORM FORMS, TO GET A GOOD VIEW C: