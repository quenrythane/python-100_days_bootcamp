from selenium.webdriver.common.by import By
from time import sleep
import os
from Driver import driver


class Bot:
    def __init__(self):
        root_path_1 = r"C:\Users\Thane Art\Desktop\Projekty\Nauka Pythona\100_days_bootcamp\days_41-50"
        root_path_2 = r"day 48 - Selenium Webdriver\automated_bot_cookie_clikcer\cookie_saves"
        bakery_name = "ThaneBakery.txt"
        self.save_path = fr"{root_path_1}\{root_path_2}\{bakery_name}"
        self.cookie_button = None
        self.products_dict = {}
        self.upgrades_list = []

        self.choose_language()
        self.load_save()
        self.cookie_button = driver.driver.find_element(by=By.ID, value="bigCookie")

    def choose_language(self):
        sleep(1)
        choose_language = driver.driver.find_element(by=By.ID, value="langSelect-EN")
        choose_language.click()
        sleep(5)  # need to wait for the page to load

    def load_save(self):
        options_button = driver.driver.find_element(by=By.CSS_SELECTOR, value="#prefsButton div.subButton")
        options_button.click()
        sleep(1)
        load_save = driver.driver.find_element(by=By.ID, value="FileLoadInput")
        load_save.send_keys(self.save_path)
        sleep(2)
        # self.delete_old_save()

    def delete_old_save(self):
        if os.path.exists(self.save_path):
            os.remove(self.save_path)

    def save_game(self):
        save_game = driver.driver.find_element(by=By.LINK_TEXT, value="Save to file")
        save_game.click()
        sleep(1)

    def clicking_cookie(self, times):
        # self.cookie_button = self.driver.find_element(by=By.ID, value="bigCookie")
        for i in range(times):
            self.cookie_button.click()

    def get_cookie_score(self):
        # thousands: 132,000
        # millions: 19.000 millions
        # billions: 19.000 billions

        cookie_score_list = driver.driver.find_element(by=By.ID, value="cookies").text.split()
        cookies_score = int(cookie_score_list[0].replace(",", "").replace(".", ""))

        multiplier = cookie_score_list[1]
        if multiplier != "cookies":
            if multiplier == "million":
                cookies_score *= 10 ** 6
            elif multiplier == "billion":
                cookies_score *= 10 ** 9
            elif multiplier == "trillion":
                cookies_score *= 10 ** 12

        return cookies_score

    def convert_price_to_int(self, price: str) -> int:
        price = price.replace(",", "").split()
        try:
            if price[1] == 'million':
                price = float(price[0]) * 10 ** 6
            elif price[1] == 'billion':
                price = float(price[0]) * 10 ** 9
            elif price[1] == 'tillion':
                price = float(price[0]) * 10 ** 12
        except IndexError:
            price = float(price[0])

        return int(price)

    def update_products_dict(self):
        # really last item will be enough

        # .product  .unlocked/.locked - see name/don`t see name
        # .enabled/.disabled - can afford to buy/can't afford to buy
        products_table_rows = driver.driver.find_elements(
            by=By.CSS_SELECTOR, value="div#products.storeSection div.product.unlocked.enabled div.content")

        self.products_dict = {}
        for i, row in enumerate(products_table_rows):
            try:
                name, price, owned = row.text.split("\n")
            except ValueError:
                name, price = row.text.split("\n")
                owned = "0"

            self.products_dict[f"product{i}"] = {
                "id": f"product{i}",
                "name": name,  # name div.productName
                "price": self.convert_price_to_int(price),  # price span.price
                "owned": int(owned),  # owned div.owned
            }
            print(self.products_dict[f"product{i}"])
        print("updated products list\n")

    def update_upgrades_list(self):
        self.upgrades_list = driver.driver.find_elements(
            by=By.CSS_SELECTOR, value="div#upgrades.storeSection div.crate.upgrade.enabled")
        print(self.upgrades_list)
        print("updated upgrades list\n")

    def try_buy_product(self):
        try:
            product = list(self.products_dict.values())[-1]
            driver.driver.find_element(by=By.CSS_SELECTOR, value=f"div.product.unlocked.enabled#{product['id']}").click()
            print(f"Bought product: {product['name']}")
        except:
            pass

    def try_buy_upgrade(self):
        try:
            self.upgrades_list[0].click()
            print(f"Bought upgrade")
        except:
            pass

    def try_catch_golden_cookie(self):
        try:
            driver.driver.find_element(by=By.CSS_SELECTOR, value="div#shimmers div.shimmer").click()
            print("Caught golden cookie")
        except:
            pass


cookie_bot = Bot()
