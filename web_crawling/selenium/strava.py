from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = 'C:\Program Files (x86)\Google\Chrome\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.strava.cz/strava/")
jedalen = driver.find_element_by_id("prihlaseni_jidelna").send_keys("9083")
driver.find_element_by_id("prihlaseni_uzivatel").send_keys("Blaž7887")
driver.find_element_by_id("prihlaseni_heslo").send_keys("7887")
x = driver.find_elements_by_class_name("prihlaseni-prihlasit")[0]
try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "prihlaseni_prihlasit"))
    )
    button.click()
except:
    print('')

uzivatele=[{"nazev":"Uživatel 1","jidelna":"","jmeno":""}]