from selenium import webdriver
from selenium.webdriver.common.by import By # Very important to import this
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chrome driver download https://chromedriver.chromium.org/downloads
# i love stackoverflow xd
# https://stackoverflow.com/questions/47148872/webdrivers-executable-may-have-wrong-permissions-please-see-https-sites-goo
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python

product_url = "https://www.amazon.de/-/en/Marvel-Heroes-Guardians-Avengers-Spaceship/dp/B098425PT1/ref=sr_1_3?crid=1DNXDPGYT6HC8&keywords=guardians+of+the+galaxy+lego&qid=1659636947&sprefix=guardians+of+the+galaxy+leg%2Caps%2C146&sr=8-3"

chrome_driver_path = 'C:\\Users\\Thane Art\\dev\\Tools\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(product_url)
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen").text
# price2 = driver.find_element(by=By.CLASS_NAME, value="a-price").text
price3 = driver.find_element(By.CLASS_NAME, "a-offscreen").get_attribute("innerHTML")
print(price3)


# drive.close()  # close tab
# drive.quit()  # close browser
