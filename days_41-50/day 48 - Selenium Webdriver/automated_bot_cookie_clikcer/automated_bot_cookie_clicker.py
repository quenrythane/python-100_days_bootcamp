from time import sleep
from Bot import cookie_bot
from Driver import driver
from selenium.webdriver.common.by import By


cookie_bot.clicking_cookie(20)

products_table = driver.driver.find_element(by=By.CSS_SELECTOR, value="div#products.storeSection")
products_table_rows = products_table.find_elements(by=By.CLASS_NAME, value="unlocked")  # this works
# .product  .unlocked/.locked - see name/don`t see name .enabled/.disabled - can afford to buy/can't afford to buy
products_table_rows = products_table.find_elements(by=By.CLASS_NAME, value="product.unlocked")  # this also works
products_table_rows = products_table.find_elements(by=By.CSS_SELECTOR, value="div.product.unlocked")  # this also works
products_table_rows = driver.driver.find_elements(by=By.CSS_SELECTOR, value="div#products.storeSection div.product.unlocked")

print("-"*20)
for row in products_table_rows:
    print(row.find_element(by=By.CSS_SELECTOR, value="div.content div.title"))
    print(row.find_element(by=By.CSS_SELECTOR, value="div.content div.title").text)


# name div.productName
# price span.price
# owned div.owned

print("pre exit")
sleep(100)
print("exit")
