from selenium import webdriver
from selenium.webdriver.common.by import By         
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep
from usefulkeys import email, password, phone


URL = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'
ACCOUNT_EMAIL = email
ACCOUNT_PASSWORD = password
PHONE = phone


# Keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
driver.get(URL)


# Sign in Button
sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)


# SELECT APPLY BUTTON
try:
    apply = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ember159"]/span'))
    )
    apply.click()
except Exception:
    print(f"Error trying to apply job: {Exception}")    
    

# PHONE INPUT
try:
    phoneNumber = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3810674944-111356421-phoneNumber-nationalNumber"]'))
    )
    phoneNumber.click()
except Exception:
    print(f"Error trying to input phone number: {Exception}")  


# SUBMIT THE JOB
try:
    submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ember392"]/span'))
    )
    submit.click()
except Exception:
    print(f"Error trying to submit: {Exception}")  