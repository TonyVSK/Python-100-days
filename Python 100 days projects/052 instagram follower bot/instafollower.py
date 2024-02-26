from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

URL = 'https://www.speedtest.net'

#1. Create a class called InstaFollower
class Instafollower:
    def __init__(self) -> None:
    # 2. In the init() method, create the Selenium driver .
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_option) # we will work with chrome
        self.driver.get(URL)
        self.login()
        self.find_followers()
        self.follow()



    # 3. Create three methods - login() and find_followers() and follow().
    def login(self):
        ...


    def find_followers(self):
        ...


    def follow(self):
        ...