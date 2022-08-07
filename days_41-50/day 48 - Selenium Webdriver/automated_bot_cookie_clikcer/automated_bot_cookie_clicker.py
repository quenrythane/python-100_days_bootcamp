from time import sleep
from Bot import cookie_bot
from Products import products
from Driver import driver
from selenium.webdriver.common.by import By

print(4)
sleep(3)

cookie_bot.clicking_cookie(20)
# print(products.products_web_component)
# driver.driver.find_element(by=By.CSS_SELECTOR, value="div#products.storeSection")
x = driver.driver.find_element(by=By.ID, value="bigCookie")

print(5)
sleep(3)

raz = driver.driver.find_element(by=By.CSS_SELECTOR, value="div#products.storeSection")
print(raz)

dwa = products.products_web_component
print(dwa)

sleep(100)
print("exit")
