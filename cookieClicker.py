from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")



cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"
closable = "close"
bakery = "bakeryName"
bakeryNameInput = "bakeryNameInput"
newBakeryName = "Asaysopensesame"

counter = 100 #amount of clicks before checking to buy things


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, cookie_id))).click()
click_me = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, cookie_id)))##


cycle = 0



preferences = driver.find_element(By.ID,"prefsButton")
actions = ActionChains(driver)
actions.move_to_element(preferences).perform()

#driver.execute_script("Game.RuinTheFun();")

while True:

    upgrade_list = driver.find_elements(By.XPATH,"//*[starts-with(@id,'upgrade') and @class='crate upgrade enabled'] ")
    if len(upgrade_list) > 0:    
        upgrade_to_buy = upgrade_list[0].get_attribute("id")
        data_id = driver.find_element(By.ID, upgrade_to_buy).get_attribute("data-id")
        if data_id != "84": #check that the Elder Covenant isn't accidentally bought
            driver.find_element(By.ID, upgrade_to_buy).click()

    product_list = driver.find_elements(By.XPATH,"//*[starts-with(@id,'product') and @class='product unlocked enabled'] ")

    #will cycle between buying the most expensive and least expensive facilities available
    if len(product_list) > 0:
        if cycle % 2 == 0:
            product_to_buy = product_list[-1].get_attribute("id")
        else:
            product_to_buy = product_list[0].get_attribute("id")
        driver.find_element(By.ID, product_to_buy).click()


    

    for i in range(counter, 0, -1):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, cookie_id))).click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))

    try:
        close_tab = driver.find_element(By.CLASS_NAME,closable).click()
    except:
        continue   
    cycle += 1