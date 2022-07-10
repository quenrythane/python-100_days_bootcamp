import smtplib
import ssl
import datetime as dt
import random




now = dt.datetime.now()
if now.weekday() == 0:
    # prepare quote
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    # get access data
    with open("access_data.txt", "r") as file:
        access_data = [line.split(": ") for line in file.read().splitlines()]

        SENDER = access_data[0][1]
        email_password = access_data[1][1]  # don't need this
        PASSWORD = access_data[2][1]  # app password

    # prepare email message and recipients
    email_message = f"Subject: Motivation quote\n\n{quote}"
    receiver_email = "artur.babinski.g@gmail.com"

    # create a secure SSL context and send email
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl_context) as smtp_connection:
        smtp_connection.login(user=SENDER, password=PASSWORD)
        smtp_connection.sendmail(from_addr=SENDER, to_addrs=receiver_email, msg=email_message)

    print("Email sent!")


