
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    message = f'Hey @Myinternet, the download speed is about {download_speed}, solve this now!'
    URL2 = 'https://twitter.com/home?lang=pt' # I'm from Brazil :P


    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)

    driver2 = webdriver.Chrome(options=chrome_option) 
    driver2.get(URL)



    square = driver2.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    square.send_keys(message)


    submit_button = driver2.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div')
    submit_button.click()