import smtplib
import ssl

# get access data
with open("../../days_31-40/day 32 - Automated Birthday Email/access_data.txt", "r") as file:
    access_data = [line.split(": ") for line in file.read().splitlines()]
    SENDER = access_data[0][1]
    PASSWORD = access_data[2][1]  # app password

print(PASSWORD)


def send_message(email, message):
    # create a secure SSL context and send email
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl_context) as smtp_connection:
        smtp_connection.login(user=SENDER, password=PASSWORD)
        smtp_connection.sendmail(from_addr=SENDER,
                                 to_addrs=email,
                                 msg=f"Subject:Subject day 60\n\n{message}"
                                 )
