import requests
import os
from twilio.rest import Client

account_sid = "AC06f908fe364c31a210ec2e1126488204"
auth_token = "12d3a5fbd5cabb198ee731d672893a85"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "TO0X2Y6WJQCOLRNQ"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
NEWS_API_KEY = "055fc7bc7a774a0c96099dea6d6124ec"

news_parameters = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API_KEY
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
http_code = stock_response.status_code
stock_response.raise_for_status()
news_data = stock_response.json()["Time Series (Daily)"]
news_data_list = [value for (key, value) in news_data.items()]

yesterday_closing = float(news_data_list[0]["4. close"])
yesterday1_closing = float(news_data_list[1]["4. close"])

difference = yesterday_closing - yesterday1_closing
positive_difference = abs(difference)
percentage_difference = round((difference / yesterday_closing) * 100)

if percentage_difference > 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_http_code = news_response.status_code
    news_response.raise_for_status()
    news_data = news_response.json()
    all_articles = news_data["articles"]

    articles_list = all_articles[:3]

    new_list = [data["title"] for data in articles_list]

    description_list = [data["description"] for data in articles_list]

    client = Client(account_sid, auth_token)

    message1 = client.messages \
        .create(
        body=f"{COMPANY_NAME}: 🔺{percentage_difference}\n%Headline: {new_list[0]}\nBrief: {description_list[0]}",
        from_="+19379000381",
        to="+254738293178"
    )

    message2 = client.messages \
        .create(
        body=f"{COMPANY_NAME}: 🔺{percentage_difference}\n%Headline: {new_list[1]}\nBrief: {description_list[1]}",
        from_="+19379000381",
        to="+254738293178"
    )

    message3 = client.messages \
        .create(
        body=f"{COMPANY_NAME}: 🔺{percentage_difference}\n%Headline: {new_list[2]}\nBrief: {description_list[2]}",
        from_="+19379000381",
        to="+254738293178"
    )


