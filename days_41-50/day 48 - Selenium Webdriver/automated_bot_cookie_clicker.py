from selenium import webdriver
from selenium.webdriver.common.by import By # Very important to import this
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def get_cookie_score():
    cookie_count = driver.find_element(by=By.ID, value="cookies")
    cookie_score_list = cookie_count.text.split()
    cookie_score = int(cookie_score_list[0].replace(",", ""))
    if cookie_score_list[1] != "cookies":


    cookie_score.replace(",", "")
    return cookie_score


url = "https://orteil.dashnet.org/cookieclicker/"
chrome_driver_path = 'C:\\Users\\Thane Art\\dev\\Tools\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
sleep(3)
# choose_language
choose_language = driver.find_element(by=By.ID, value="langSelect-EN")
choose_language.click()
sleep(3)

# click_cookie
cookie_button = driver.find_element(by=By.ID, value="bigCookie")
for i in range(10):
    cookie_button.click()

for i in range(100):
    cookie_score = get_cookie_score()
    print(cookie_score)
    sleep(1)
    cookie_button.click()

sleep(1)
print(get_cookie_score())



sleep(100)
print("exit")
