import requests as req
from twilio.rest import Client


## STEP 1: Use https://www.alphavantage.co
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "TRA7J4P5E8UCUOR"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
data = req.get(STOCK_ENDPOINT, params=stock_parameters).json()

yesterday_date, day_before_yesterday_date = list(data["Time Series (Daily)"].keys())[:2]
yesterday_price = float(data["Time Series (Daily)"][yesterday_date]["4. close"])
day_before_yesterday_price = float(data["Time Series (Daily)"][day_before_yesterday_date]["4. close"])

change_in_percent = abs(yesterday_price - day_before_yesterday_price) / yesterday_price * 100
if change_in_percent >= 5:
    print("Get News")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
NEWS_API_KEY = "2f136339c81d495c8e291522470286fa"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_parameters = {
    # "q": COMPANY_NAME,
    "qInTitle": COMPANY_NAME,
    "from": day_before_yesterday_date,
    "apiKey": NEWS_API_KEY,
}
news = req.get(NEWS_ENDPOINT, params=news_parameters).json()


def count_change():
    change = yesterday_price - day_before_yesterday_price
    if change > 0:
        change_message = f"🔺{change_in_percent:.2f}%"
    else:
        change_message = f"🔻{change_in_percent:.2f}%"
    return change_message


def prepare_message():
    message = f"{STOCK_NAME}: {count_change()}\n"  \
              f"{article['title']}\n" \
              f"{article['url']}"
    return message


message_articles = []
for article in news["articles"][:3]:
    message_articles.append(prepare_message())


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and url to your phone number.
# https://www.twilio.com/
with open("twilio_auth.txt", "r") as file:
    account_sid, auth_token, twilio_number, my_number = file.read().splitlines()
    print(account_sid)
    print(auth_token)

client = Client(account_sid, auth_token)

message = client.messages.create(
                     body=message_articles[0],
                     from_=twilio_number,
                     to=my_number
                 )

print(message_articles[0])
print(message.sid)
print(message.status)


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
