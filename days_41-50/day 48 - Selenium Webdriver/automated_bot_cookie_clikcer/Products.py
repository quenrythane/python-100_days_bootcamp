from selenium.webdriver.common.by import By
from Driver import driver
from time import sleep


print(1)
sleep(3)


class Products:
    def __int__(self):
        self.products_dict = {}
        self.products_web_component = driver.driver.find_element(by=By.CSS_SELECTOR, value="div#products.storeSection")


class Product:
    def __int__(self):
        self.product_data = products.products_web_component.find_elements(by=By.CSS_SELECTOR, value="div.product")[0]
        # self.product_name = self.product_data.split()[0]

print(2)
sleep(3)

products = Products()
product = Product()
print(3)
sleep(3)
