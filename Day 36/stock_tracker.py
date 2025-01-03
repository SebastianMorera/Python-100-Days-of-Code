from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

STOCK_API_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_stock_data(symbol: str) -> (float, float, float, bool):
    stock_api_key = os.environ.get("ALPHA_VANTAGE_STOCK_API_KEY")
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": stock_api_key,
    }

    response = requests.get(url=STOCK_API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    list_of_days = [day for day in data["Time Series (Daily)"]]
    yesterday_closing_price = float(data["Time Series (Daily)"][list_of_days[0]]["4. close"])
    two_days_ago_closing_price = float(data["Time Series (Daily)"][list_of_days[1]]["4. close"])
    diff_percent = abs(yesterday_closing_price - two_days_ago_closing_price) / yesterday_closing_price * 100
    if yesterday_closing_price - two_days_ago_closing_price >= 0:
        positive_diff = True
    else:
        positive_diff = False

    return yesterday_closing_price, two_days_ago_closing_price, diff_percent, positive_diff


def get_news(company_name: str) -> list:
    news_api_key = os.environ.get("NEWS_API_KEY")
    params = {
        "apiKey": news_api_key,
        "qInTitle": company_name
    }
    response = requests.get(url=NEWS_API_URL, params=params)
    response.raise_for_status()
    articles = response.json()["articles"]

    return articles[:3]


def send_sms(message: str):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+16282126440',
        body=message,
        to='+18777804236'
    )
    print(f"SMS text sent with status {message.status}")


def stock_tracker(stock: str) -> None:
    yesterday_closing_price, two_days_ago_closing_price, diff_percent, positive_diff = get_stock_data(stock)

    if diff_percent >= 5:
        news = get_news(stock)
        diff_emoji = "🔺" if positive_diff else "🔻"

        for article in news:
            price_diff = f"{stock}: {diff_emoji}{diff_percent:.2f}%\n"
            headline = f"Headline: {article["title"]}\n"
            brief = f"Brief: {article["description"]}"
            message = f"{price_diff}{headline}{brief}"
            send_sms(message)


if __name__ == "__main__":
    load_dotenv()
    stock_tracker(STOCK)
