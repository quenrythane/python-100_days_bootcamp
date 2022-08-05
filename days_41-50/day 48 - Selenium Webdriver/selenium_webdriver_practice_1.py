from selenium import webdriver
from selenium.webdriver.common.by import By # Very important to import this
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.python.org/"
chrome_driver_path = 'C:\\Users\\Thane Art\\dev\\Tools\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)
events = driver.find_elements(by=By.CSS_SELECTOR, value="div .event-widget .shrubbery .menu li")

events_dict = {}
for index, event in enumerate(events):
    event_time = event.find_element(by=By.CSS_SELECTOR, value="time").text
    event_name = event.find_element(by=By.CSS_SELECTOR, value="a").text
    events_dict[index] = {"time": event_time, "name": event_name}
print(events_dict)


events_dict_compr = {index: {"time": event.find_element(by=By.CSS_SELECTOR, value="time").text,
                 "name": event.find_element(by=By.CSS_SELECTOR, value="a").text}
         for index, event in enumerate(events)}
print(events_dict_compr)
