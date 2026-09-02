import datetime as dt
import smtplib
import random

my_email = "softway_practice@gmail.com"
my_password = "gbefunbotegaurus"

with open("../Birthday Wisher (Day 32) start/quotes.txt", "r") as quotes:
    quotes_list = quotes.readlines()
    # print(quotes_list)

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    today_quote = random.choice(quotes_list)
    # print(today_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="softway_testing@yahoo.com",
            msg=f"Subject: New week motivation\n\n {today_quote}"
        )