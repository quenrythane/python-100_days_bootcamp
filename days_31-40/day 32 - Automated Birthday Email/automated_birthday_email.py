import smtplib
import ssl




receiver_email = "artur.babinski.g@gmail.com"
email_subject = "Subject test"
email_body = "Hello world test"
email_message = f"Subject:{email_subject}\n\n{email_body}"


"""
1. turn on 2fa
2. create an app password
"""

ssl_context = ssl.create_default_context()  # create secure socket layer context
with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl_context) as smtp_connection:  # start smpt
    smtp_connection.login(user=SENDER, password=PASSWORD)  # login
    smtp_connection.sendmail(from_addr=SENDER, to_addrs=receiver_email, msg=email_message)  # send message
