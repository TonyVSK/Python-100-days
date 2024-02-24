
from selenium import webdriver
from selenium.webdriver.common.by import By         
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = 'https://tinder.com'

# Keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
driver.get(URL)

# Login in Button
sleep(2)
log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="c-1398387530"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in_button.click()

# Sign in with Facebook
sleep(5)
facebook_button = driver.find_element(by=By.XPATH, value='//*[@id="c-1177047094"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
facebook_button.click()

# Location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Site cookies
cookies = driver.find_element(By.XPATH, '//button[contains(string(), "Allow all cookies")]')
cookies.click()

# like button xpath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
# SELECT APPLY BUTTON
# try:
#     apply = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="ember159"]/span'))
#     )
#     apply.click()
# except Exception:
#     print(f"Error trying to apply job: {Exception}")    
    


