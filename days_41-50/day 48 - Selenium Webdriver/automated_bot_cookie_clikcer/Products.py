# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# import os
from Bot import cookie_bot


class Products:
    def __int__(self):
        self.products_dict = {}
        self.products_web_component = cookie_bot.find_element(by=By.ID, value="products")

    def add_product(self, product_name, product_price):
        pass


class Product:
    def __int__(self):
        self.product_data = products.products_web_component.find_elements(by=By.CSS_SELECTOR, value="div.product")[0]
        # self.product_name = self.product_data.split()[0]



sleep(10)
products = Products()
product = Product()
print(product.product_data)
