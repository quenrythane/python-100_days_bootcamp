from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

class Bot:
    def __init__(self):
        self.url = "https://orteil.dashnet.org/cookieclicker/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.root_path = r"C:\Users\Thane Art\Desktop\Projekty\Nauka Pythona\100_days_bootcamp"
        self.save_path = fr"{self.root_path}\days_41-50\day 48 - Selenium Webdriver\cookie_saves\PirateMuffinBakery.txt"
        self.cookie_button = None
        # chrome_driver_path = 'C:\\Users\\Thane Art\\dev\\Tools\\chromedriver.exe'
        # after update dont need this anymore

        self.prepare_page()
        self.choose_language()
        self.load_save()
        self.cookie_button = self.driver.find_element(by=By.ID, value="bigCookie")

    def prepare_page(self):
        self.driver.get(self.url)
        sleep(1)

    def choose_language(self):
        choose_language = self.driver.find_element(by=By.ID, value="langSelect-EN")
        choose_language.click()
        sleep(5)  # need to wait for the page to load

    def load_save(self):
        options_button = self.driver.find_element(by=By.CSS_SELECTOR, value="#prefsButton div.subButton")
        options_button.click()
        sleep(1)
        load_save = self.driver.find_element(by=By.ID, value="FileLoadInput")
        load_save.send_keys(self.save_path)
        sleep(1)

    def delete_old_save(self):
        if os.path.exists(self.save_path):
            os.remove(self.save_path)

    def save_game(self):
        save_game = self.driver.find_element(by=By.LINK_TEXT, value="Save to file")
        save_game.click()
        sleep(1)
        # save_game.send_keys("PirateMuffinBakery")
        # save_game.send_keys(Keys.ENTER)
        # save_game.send_keys(Keys.ARROW_LEFT)
        # save_game.send_keys(Keys.ENTER)

    def clicking_cookie(self, times):
        # self.cookie_button = self.driver.find_element(by=By.ID, value="bigCookie")
        for i in range(times):
            self.cookie_button.click()

    def get_cookie_score(self):
        # thousands: 132,000
        # millions: 19.000 millions
        # billions: 19.000 billions

        cookie_score_list = self.driver.find_element(by=By.ID, value="cookies").text.split()
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


cookie_bot = Bot()
cookie_bot.clicking_cookie(20)





sleep(100)
print("exit")
