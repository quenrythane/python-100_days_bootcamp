from selenium import webdriver
from selenium.webdriver.common.by import By # Very important to import this
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = 'C:\\Users\\Thane Art\\dev\\Tools\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)
"""
<input name="fName" type="text" class="form-control top" placeholder="First Name" required="" autofocus="">
this is how to find attribute of element in css_selector
input[name='fName']
"""
first_name = driver.find_element(by=By.CSS_SELECTOR, value="input[name='fName']")
first_name.send_keys("John")
last_name = driver.find_element(by=By.CSS_SELECTOR, value="input[name='lName']")
last_name.send_keys("Wick")
email = driver.find_element(by=By.CSS_SELECTOR, value="input[name='email']")
email.send_keys("JW@jw.com")
email.send_keys(Keys.ENTER)


print("exit")