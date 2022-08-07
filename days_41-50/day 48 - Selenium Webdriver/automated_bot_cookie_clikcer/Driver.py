from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Driver:
    def __init__(self):
        self.url = "https://orteil.dashnet.org/cookieclicker/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)
        sleep(1)


driver = Driver()
