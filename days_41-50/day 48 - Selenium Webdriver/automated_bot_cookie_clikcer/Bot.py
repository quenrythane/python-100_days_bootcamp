from selenium.webdriver.common.by import By
from time import sleep
import os
from Driver import driver


class Bot:
    def __init__(self):
        root_path = r"C:\Users\Thane Art\Desktop\Projekty\Nauka Pythona\100_days_bootcamp\days_41-50\day 48 - Selenium Webdriver"
        self.save_path = fr"{root_path}\automated_bot_cookie_clikcer\cookie_saves\PirateMuffinBakery.txt"
        self.cookie_button = None
        self.products_dict = {}

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


cookie_bot = Bot()
