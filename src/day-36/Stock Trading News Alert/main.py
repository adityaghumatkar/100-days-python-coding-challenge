STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

import requests

ALPHAVANTAGE_API_KEY = "1ADHA2YPTS2616XB"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]


data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
# print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

positive_difference_stock_closing_prices = abs(
    float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
# print(positive_difference_stock_closing_prices)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

delta_percentage_change = positive_difference_stock_closing_prices / day_before_yesterday_closing_price * 100
# print(delta_percentage_change)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
import datetime as dt
from twilio.rest import Client
NEW_API_KEY = "72e08bf6f56f424783854f849066dfaa"
if delta_percentage_change > 2:
    # print("great news")
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    now = dt.datetime.now()
    from_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEW_API_KEY
    }
    response = requests.get(url=NEWS_ENDPOINT,params=parameters)
    response.raise_for_status()
    data = response.json()


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    all_articles = data["articles"]
    # print(all_articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    top_three_articles = all_articles[:3]
    # print(top_three_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_article = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in top_three_articles]

#TODO 9. - Send each article as a separate message via Twilio.


    account_sid = "AC6994b496f641dcc57234fce48b080bc9"
    auth_token = "9626cc7eaa6cd9d2cac9ddad16e52704"

    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            from_="+12516510630",
            body=article,
            to="+919545767032"
        )

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
