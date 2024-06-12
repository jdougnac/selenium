from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service=service)


username = "standard_user"
password = "secret_sauce"
sortBy = "Price (high to low)"
fleeceID = "add-to-cart-sauce-labs-fleece-jacket"
shirtID = "add-to-cart-test.allthethings()-t-shirt-(red)"
lightID = "add-to-cart-sauce-labs-bike-light"
firstName = "Pedro"
lastName = "Perez"
zipCode = "1754831"

driver.get("https://www.saucedemo.com/")


user = driver.find_element(By.NAME, "user-name")
user.clear()
user.send_keys(username)

passW = driver.find_element(By.NAME,"password")
passW.clear()
passW.send_keys(password)


print('AAA')


login = driver.find_element(By.ID,"login-button")

login.click()
print('BBB')

sort = driver.find_element(By.CLASS_NAME,"product_sort_container")
drop = Select(sort)
drop.select_by_visible_text(sortBy)

print('CCC')

fleece = driver.find_element(By.ID,fleeceID)
fleece.click()

shirt = driver.find_element(By.ID,shirtID)
shirt.click()

light = driver.find_element(By.ID, lightID)
light.click()


print('EEE')

cart = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
cart.click()

checkout = driver.find_element(By.ID,"checkout")
checkout.click()

print('FFF')
#first-name last-name postal-code
first = driver.find_element(By.ID,"first-name")
first.clear()
first.send_keys(firstName)

last = driver.find_element(By.ID,"last-name")
last.clear()
last.send_keys(lastName)

zip = driver.find_element(By.ID,"postal-code")
zip.clear()
zip.send_keys(zipCode)

cont = driver.find_element(By.ID,"continue")
cont.click()

finish = driver.find_element(By.ID,"finish")
finish.click()

time.sleep(5)

driver.quit()