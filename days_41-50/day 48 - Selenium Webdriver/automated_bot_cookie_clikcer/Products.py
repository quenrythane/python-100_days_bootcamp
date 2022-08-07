from selenium.webdriver.common.by import By
from Driver import driver
from time import sleep


class Products:
    def __int__(self):
        self.products_dict = {}
        self.products_web_component = driver.driver.find_element(by=By.CSS_SELECTOR, value="div#products.storeSection")


class Product:
    def __int__(self):
        self.product_data = products.products_web_component.find_elements(by=By.CSS_SELECTOR, value="div.product")[0]


products = Products()
product = Product()

