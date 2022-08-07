from time import sleep
from Bot import cookie_bot
from Driver import driver
from selenium.webdriver.common.by import By


cookie_bot.clicking_cookie(20)


def convert_price_to_int(price: str) -> int:
    price = price.replace(",", "").split()
    try:
        if price[1] == 'million':
            price = float(price[0]) * 10 ** 6
        elif price[1] == 'priceillion':
            price = float(price[0]) * 10 ** 9
        elif price[1] == 'tillion':
            price = float(price[0]) * 10 ** 12
    except IndexError:
        price = float(price[0])

    return int(price)


def update_product_list():
    # .product  .unlocked/.locked - see name/don`t see name .enabled/.disabled - can afford to buy/can't afford to buy
    products_table_rows = driver.driver.find_elements(
        by=By.CSS_SELECTOR, value="div#products.storeSection div.product.unlocked div.content")

    for i, row in enumerate(products_table_rows):
        try:
            name, price, owned = row.text.split("\n")
        except ValueError:
            name, price = row.text.split("\n")
            owned = "0"

        cookie_bot.products_dict[f"product{i}"] = {
            "id": f"product{i}",
            "name": name,  # name div.productName
            "price": convert_price_to_int(price),  # price span.price
            "owned": int(owned),  # owned div.owned
        }
        print(cookie_bot.products_dict[f"product{i}"])


print("-"*20)
update_product_list()

print("-*"*20)
print(cookie_bot.products_dict)

print("pre exit")
sleep(100)
print("exit")
