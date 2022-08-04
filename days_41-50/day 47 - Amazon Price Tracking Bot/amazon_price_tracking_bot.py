from bs4 import BeautifulSoup
import requests as req
import smtplib


ALERT_PRICE = 100.0
PRODUCT_URL = "https://www.amazon.de/-/en/Marvel-Heroes-Guardians-Avengers-Spaceship/dp/B098425PT1/ref=sr_1_3?crid=1DNXDPGYT6HC8&keywords=guardians+of+the+galaxy+lego&qid=1659636947&sprefix=guardians+of+the+galaxy+leg%2Caps%2C146&sr=8-3"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7"
}

response = req.get(PRODUCT_URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find("span", class_="a-offscreen").text
price = float(price[1:])
product_title = soup.find("span", id="productTitle").text.strip()


if price <= ALERT_PRICE:
    # prepare access data
    with open("access_data.txt", "r") as file:
        access_data = [line.split(": ") for line in file.read().splitlines()]

        SENDER = access_data[0][1]
        PASSWORD = access_data[2][1]  # app password

        receiver_email = "artur.babinski.g@gmail.com"
        email_subject = f"Anazon price alert - {product_title}"
        email_body = f"{product_title} is now {price}\n{PRODUCT_URL}"
        email_message = f"Subject:{email_subject}\n\n{email_body}"


"""
    # create a secure SSL context and send email
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl_context) as smtp_connection:
        smtp_connection.login(user=SENDER, password=PASSWORD)
        smtp_connection.sendmail(from_addr=SENDER, to_addrs=receiver_email, msg=email_message)


    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
"""
