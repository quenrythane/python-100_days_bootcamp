from time import sleep
from Bot import cookie_bot
from Driver import driver
from selenium.webdriver.common.by import By


cookie_bot.clicking_cookie(20)

# .product  .unlocked/.locked - see name/don`t see name .enabled/.disabled - can afford to buy/can't afford to buy

print("-"*20)

def update_product_list():
    products_table_rows = driver.driver.find_elements(
        by=By.CSS_SELECTOR, value="div#products.storeSection div.product.unlocked div.content")

    for i, row in enumerate(products_table_rows):
        try:
            name, price, owned = row.text.split("\n")
        except ValueError:
            name, price, ownde = row.text.split("\n"), "0"

        cookie_bot.products_dict[f"product{i}"] = {
            "id": f"product{i}",
            "name": name,  # name div.productName
            "price": price,  # price span.price
            "owned": owned,  # owned div.owned
        }
        print(cookie_bot.products_dict[f"product{i}"])

print("-*"*20)

print(cookie_bot.products_dict)

print("pre exit")
sleep(100)
print("exit")
