from selenium import webdriver
from selenium.webdriver.common.by import By # Very important to import this
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
# stop closing window after test
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

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
# author_click.click()

# SEARCH INPUT
book_name_input = "Alchemia duchowego rozwoju. Inteligencja duchowa dla zaawansowanych"
search_for_book = driver.find_element(by=By.CSS_SELECTOR, value="div.css-1ya4oyk-root-6 input")
print(search_for_book.get_dom_attribute("placeholder"))

search_for_book.click()
search_for_book.send_keys(book_name_input)
search_for_book.send_keys(Keys.ENTER)
"""
books = driver.find_element(by=By.CSS_SELECTOR, value="h2.product-title")
print(books.get_attribute("innerHTML"))
"""
# print("exit")
