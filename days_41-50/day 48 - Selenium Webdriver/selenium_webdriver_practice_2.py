from selenium import webdriver
from selenium.webdriver.common.by import By # Very important to import this
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.empik.com/alchemia-duchowego-rozwoju-inteligencja-duchowa-dla-zaawansowanych-gibas-jaroslaw,p1220161977,ebooki-i-mp3-p"
chrome_driver_path = 'C:\\Users\\Thane Art\\dev\\Tools\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)


book_title = driver.find_element(by=By.CSS_SELECTOR, value="h1.productBaseInfo__title").text
book_title = book_title.split(" (")[0]
print(book_title)

book_authors = driver.find_elements(by=By.CSS_SELECTOR, value="span.pDAuthorList")
book_authors = ", ".join([author.text for author in book_authors])
print(book_authors)

book_data = driver.find_element(by=By.CSS_SELECTOR, value="table.productDataTable")
print(book_data.get_attribute("innerHTML"))
book_data = book_data.find_elements(by=By.CLASS_NAME, value="attributeDetailsValue")
print("-" * 200)

for row in book_data:
    print(row.text)
    print(row.get_attribute("innerHTML"))
    print("-" * 20)

book_title = book_data[1].text
book_authors = book_data[2].find_element(by=By.CSS_SELECTOR, value="a").text
book_publish_date = book_data[7].text.split("-")[:2]

print(book_title, book_authors, book_publish_date)