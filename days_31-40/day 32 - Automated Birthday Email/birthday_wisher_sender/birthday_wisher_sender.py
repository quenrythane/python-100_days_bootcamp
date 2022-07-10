from datetime import datetime
import pandas
import random
import smtplib
import ssl

# get access data
with open("../access_data.txt", "r") as file:
    access_data = [line.split(": ") for line in file.read().splitlines()]
    SENDER = access_data[0][1]
    PASSWORD = access_data[2][1]  # app password

# prepare data_dict with birthdays (key = (month, day, email))
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"], data_row["email"]): data_row for (index, data_row) in data.iterrows()}

# check today date
SENDER_SIGNATURE = "Artur"
today = datetime.now()
today_tuple = (today.month, today.day)

# main code
for key in birthdays_dict:
    if today_tuple == key[:2]:  # check if today is birthday
        # prepare email message
        birthday_person = birthdays_dict[key]
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])
            contents = contents.replace("[SENDER]", SENDER_SIGNATURE)

        # create a secure SSL context and send email
        ssl_context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl_context) as smtp_connection:
            smtp_connection.login(user=SENDER, password=PASSWORD)
            smtp_connection.sendmail(from_addr=SENDER,
                                     to_addrs=birthday_person["email"],
                                     msg=f"Subject:Happy Birthday!\n\n{contents}"
                                     )
        print(f"Email sent to {birthday_person['email']}!")

