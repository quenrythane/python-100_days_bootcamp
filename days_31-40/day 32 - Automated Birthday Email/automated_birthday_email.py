import smtplib
import ssl


""" Google SMTP server details
Step 1. Enable 2-Step Verification.
Step 2. Create a new App password. Make sure you save it - it is only displayed once!
Step 3. Use the App password in your code instead of your normal password
"""

# prepare access data
with open("access_data.txt", "r") as file:
    access_data = [line.split(": ") for line in file.read().splitlines()]

    SENDER = access_data[0][1]
    email_password = access_data[1][1]  # dont need this
    PASSWORD = access_data[2][1]  # app password

receiver_email = "artur.babinski.g@gmail.com"
email_subject = "Subject test"
email_body = "Hello world test"
email_message = f"Subject:{email_subject}\n\n{email_body}"

# create a secure SSL context and send email
ssl_context = ssl.create_default_context()  # create secure socket layer context
with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl_context) as smtp_connection:  # start smpt
    smtp_connection.login(user=SENDER, password=PASSWORD)  # login
    smtp_connection.sendmail(from_addr=SENDER, to_addrs=receiver_email, msg=email_message)  # send message
