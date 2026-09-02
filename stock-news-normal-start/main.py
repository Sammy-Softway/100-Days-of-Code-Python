import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY= os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
status_code = response.status_code
all_data = response.json()
# print(data)
# print(status_code)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
required_data = all_data["Time Series (Daily)"]
data_list = [value for (key, value) in required_data.items()]
yesterday_data = data_list[0]
yesterday_closing_value = yesterday_data["4. close"]
print(yesterday_closing_value)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_value = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_value)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff_btw_closing_values = abs(float(yesterday_closing_value) - float(day_before_yesterday_closing_value))
up_down = None
if diff_btw_closing_values > 0:
    up_down = "⬆️"
else:
    up_down = "🔻"
print(diff_btw_closing_values)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round((diff_btw_closing_values / float(yesterday_closing_value)) * 100)
print(percentage_diff)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_diff) > 1:
    print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    all_news_data = news_response.json()
    articles = all_news_data["articles"]
    # print(articles)

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_three_article_list = articles[:3]
    print(first_three_article_list)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    #Headline: \n Content:
    formatted_article_list = [(f"{STOCK_NAME}: {up_down} {abs(percentage_diff)}%\n"
                               f"Headline: {article['title']} \n "
                               f"Brief: {article['description']}")
                              for article in first_three_article_list]
    print(formatted_article_list)

    #TODO 9. - Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)

    for article in formatted_article_list:
        message = client.messages.create(
            body=article,
            from_="+12694042693",
            to="+2348146191616",
        )
        print(f"Message Status: {message.status} - SID: {message.sid}")

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

