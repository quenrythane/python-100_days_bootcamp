#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


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

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])


    # create a secure SSL context and send email
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl_context) as smtp_connection:
        smtp_connection.login(user=SENDER, password=PASSWORD)
        smtp_connection.sendmail(from_addr=SENDER, 
                                 to_addrs=birthday_person["email"],
                                 msg=f"Subject:Happy Birthday!\n\n{contents}"
                                 )

