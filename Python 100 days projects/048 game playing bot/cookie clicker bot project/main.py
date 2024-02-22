from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://orteil.dashnet.org/cookieclicker/"


# Keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option) # we will work with chrome
driver.get(URL)

# First button - select idiom
try:
    # Espera até que o elemento seja clicável. Ajuste o tempo de espera conforme necessário.
    idiom = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-PT-BR"]'))
    )
    idiom.click()
except Exception:
    print(f"Erro ao tentar selecionar o idioma: {Exception}")


# Second button - site cookies
try:
    sitecookie = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/a[1]'))
    )
    sitecookie.click()
except Exception:
    print(f"Erro ao tentar selecionar o idioma: {Exception}")


# third button - cookie

wait = WebDriverWait(driver, 10)
cookie_locator = (By.CSS_SELECTOR, '#bigCookie')

cookies = 0

while True:
    wait.until(EC.element_to_be_clickable(cookie_locator))
    cookie_clicker = driver.find_element(*cookie_locator)
    cookie_clicker.click()
    cookies += 1



    # THIS CODE WILL WORK ONLY WITH THE TWO FIRSTS BOOSTS OF GAME
    # if you want the other boosts, the logic is the same: just copy and past, and replace de ID for the boost ID in html, and, of course, don't forget to chance the variables names
    # mouse clicker
    mouse_price_element = driver.find_element(By.ID, 'productPrice0')
    try:
        mouse_value = float(mouse_price_element.text)  
    except ValueError: # the text in html often apears with ",". Example, if it coosts 1100 cookies, the text will apear 1,100 . And we will need to remove the ","
        mouse_temporary_value = mouse_price_element.text
        get_number = mouse_temporary_value.replace(',', '')
        mouse_value = float(get_number.text)  
        
    grandma_value = 0
    farm_value = 0
    mine_value = 0
    factory_value = 0

    # buy mouse clickers
    if cookies >= mouse_value:
        mouse_locator = driver.find_element(By.XPATH, value='//*[@id="product0"]')
        mouse_locator.click()
        # grandma values
        grandma_element = driver.find_element(By.ID, 'productPrice1')
        try:
            grandma_value = float(grandma_element.text)  
        except ValueError:
            grandma_temporary_value = grandma_element.text
            grandma_number = grandma_temporary_value.replace(',', '')
            grandma_value = float(grandma_number.text)           
    # buy grandmas
    if cookies >= grandma_value:
        grandma_locator = driver.find_element(By.XPATH, value='//*[@id="product1"]')
        grandma_locator.click()
