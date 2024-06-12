from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service=service)


first_name = "Pedro"
last_name = "Pérez"
current_date = "6/27/2024"
continentText = "South America"
commandsText = "Switch Commands"


driver.get("https://www.techlistic.com/p/selenium-practice-form.html")


name = driver.find_element(By.NAME, "firstname")
name.clear()
name.send_keys(first_name)

lastName = driver.find_element(By.NAME,"lastname")
lastName.clear()
lastName.send_keys(last_name)

action = ActionChains(driver)

genderCheck = driver.find_element(By.ID,"sex-0")

js_code = "arguments[0].scrollIntoView();"


# Execute the JS script
driver.execute_script(js_code, genderCheck)
genderCheck.click()
print('AAA')


experience = driver.find_element(By.ID,"exp-3")

experience.click()
print('BBB')

date = driver.find_element(By.ID,"datepicker")
date.clear()
date.send_keys(current_date)

print('CCC')

prof = driver.find_element(By.ID, "profession-1")
prof.click()

tool = driver.find_element(By.ID, "tool-2")
tool.click()

continent = driver.find_element(By.ID,"continents")
drop = Select(continent)
drop.select_by_visible_text(continentText)

print('DDD')

commands = driver.find_element(By.ID,"selenium_commands")
drop = Select(commands)
drop.select_by_visible_text(commandsText)

print('EEE')
time.sleep(5)

driver.quit()