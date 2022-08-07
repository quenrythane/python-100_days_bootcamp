from selenium import webdriver
from selenium.webdriver.common.by import By # Very important to import this
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.empik.com/alchemia-duchowego-rozwoju-inteligencja-duchowa-dla-zaawansowanych-gibas-jaroslaw,p1220161977,ebooki-i-mp3-p"
chrome_driver_path = 'C:\\Users\\Thane Art\\dev\\Tools\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)
book_data = driver.find_elements(by=By.CSS_SELECTOR, value="table.productDataTable tbody tr td span.attributeDetailsValue")

title = book_data[1].get_attribute("innerHTML").strip()
author = book_data[2].find_element(by=By.CSS_SELECTOR, value="a").get_attribute("innerHTML").strip().replace("&nbsp;", " ")
date = book_data[7].get_attribute("innerHTML").strip()

# CLICK
# find link by link text and click that link
author_click = driver.find_element(by=By.LINK_TEXT, value=author)
author_click.click()

# SEARCH INPUT
book_name_input = "Alchemia duchowego rozwoju. Inteligencja duchowa dla zaawansowanych"
search_for_book = driver.find_element(by=By.CSS_SELECTOR, value="input.css-1rwl265-input-1")
print(search_for_book)
search_for_book.send_keys(book_name_input)


