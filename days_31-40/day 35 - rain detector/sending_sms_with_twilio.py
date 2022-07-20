# https://www.twilio.com/
# (989) 465-5976
# +19894655976
from twilio.rest import Client

with open("twilio_auth.txt", "r") as file:
    account_sid, auth_token, twilio_number, my_number = file.read().splitlines()
    print(account_sid)
    print(auth_token)

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=twilio_number,
                     to=my_number
                 )

print(message.sid)
print(message.status)
