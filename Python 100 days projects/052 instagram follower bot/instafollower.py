from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from keyfiles import email, password

EMAIL = email
PASSWORD = password
URL = 'https://www.instagram.com/accounts/login/'

#1. Create a class called InstaFollower
class InstaFollower:
    def __init__(self) -> None:
    # 2. In the init() method, create the Selenium driver .
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
        self.driver.get(URL)
        sleep(2) # wait page load


    # 3. Create three methods - login() and find_followers() and follow().
    def login(self):
        email_box = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_box.send_keys(EMAIL, Keys.TAB)

        password_box = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_box.send_keys(PASSWORD, Keys.ENTER)


    def find_followers(self):
        ...


    def follow(self):
        ...