from selenium import webdriver
from selenium.webdriver.common.by import By

# URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


# # Keep Chrome browser open after program finishes
# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
# driver.get(URL)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f'The price is {price_dollar.text}.{price_cents.text}')
# ## Close all browser
# driver.quit()

URL = "https://en.wikipedia.org/wiki/Main_Page"


# Keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
driver.get(URL)

times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# for time in times:
#     print(time.text)
event_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(event_articles.text)


## Close all browser
driver.quit()