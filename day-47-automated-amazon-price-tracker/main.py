from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.environ.get('LINK')
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")

# Full headers would look something like this
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Dnt": "1",
    "Priority": "u=4, i",
    "SEC-CH-UA": '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
    "SEC-CH-UA-MOBILE": "?0",
    "SEC-CH-UA-PLATFORM": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "SEC-PURPOSE": "prefetch;anonymous-client-ip",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
}

# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
# }

# Adding headers to the request
response = requests.get(URL, headers=header)
web_html = response.text

soup = BeautifulSoup(web_html, 'html.parser')
# A check if I'm getting the actual Amazon page back and not something else
# print(soup.prettify())

price_target = soup.find(name='span', class_='a-offscreen')
title_target = soup.find(name='span', id='productTitle')
# print(price_target.text)
# print(title_target.text)

price_without_dollar_sign = price_target.text.split('$')[1]
price_as_float = float(price_without_dollar_sign)
title = title_target.text.strip()
# print(price)

if price_as_float < 100:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Amazon Price Alert!\n\n "
                f"{title} is now {price_target.getText()}\n "
                f"{URL}".encode("utf-8")
        )