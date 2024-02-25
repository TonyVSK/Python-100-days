
from selenium import webdriver
from selenium.webdriver.common.by import By         
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = 'https://www.speedtest.net'

# Keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
driver.get(URL)

# Cookies site button
try:
    sleep(2)
    cookie = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
except:
    pass


# 'GO' button
sleep(2)
log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
log_in_button.click()


# speed results
try:
    sleep(35) # 35 seconds to load and see my speed
    download = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]')
    download_speed = float(download.text)
except Exception:
    print(f"Error trying to access download: {Exception}")

if download_speed < 50:
    URL2 = 'https://twitter.com/home?lang=pt' # I'm from Brazil :P

    # Keep Chrome browser open after program finishes
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
    driver.get(URL)

    # Cookies site button
    try:
        sleep(2)
        cookie = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
    except:
        pass


    # 'GO' button
    sleep(2)
    log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    log_in_button.click()


    # speed results
    try:
        sleep(35) # 35 seconds to load and see my speed
        download = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]')
        download_speed = float(download.text)
    except Exception:
        print(f"Error trying to access download: {Exception}")