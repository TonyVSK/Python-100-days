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

URL = "https://www.python.org/"


# Keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
driver.get(URL)

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)


# bug_link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# print(bug_link.text)

times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# for time in times:
#     print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for name in event_names:
#     print(name.text)
events = {}

for n in range(0, len(times)):
    events[n] = {
        "time": times[n].text,
        "name": event_names[n].text
    }

for n in range(0, len(times)):
    print(f"{events[n]}\n")


## Close all browser
driver.quit()