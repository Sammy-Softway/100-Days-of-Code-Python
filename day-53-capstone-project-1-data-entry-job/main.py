from bs4 import BeautifulSoup
import requests
import  os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

load_dotenv()

ZILLOW_URL = os.getenv("ZILLOW_CLONED_WEB")
GOOGLE_FORM_LINK = os.getenv("GOOGLE_FORM_LINK")

#Fetch HTML from the live website
response = requests.get(ZILLOW_URL)
web_html = response.content

#Parse the HTML content
soup = BeautifulSoup(web_html, 'html.parser')

addresses = soup.select(selector="div .StyledPropertyCardDataWrapper address")
address_list = [address.text.strip() for address in addresses]
# print(address_list)

prices = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
price_list = [price.text.split('+')[0].split('/')[0] for price in prices]
# It can also be rewritten as shown below because of the inconsistent format from scraping the live websites
# price_list = [price.text.split('+')[0].replace('/mo', '') for price in prices]
# print(price_list)

links = soup.select(selector="div .StyledPropertyCardDataWrapper a")
link_list = [link['href'] for link in links]
# print(link_list)

# print(len(address_list))
# print(len(price_list))
# print(len(link_list))

#-------------- STEP 2 ----------------------#
# Initialize Chrome options
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM_LINK)
sleep(2)

for index in range(len(address_list)):
    print(f"Data entry progress: {index + 1} of {len(address_list)}")

    address_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_input.send_keys(address_list[index])
    price_input.send_keys(price_list[index])
    link_input.send_keys(link_list[index])
    submit_button.click()

    try:
        another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_response.click()
        sleep(2)
    except Exception:
        driver.get(GOOGLE_FORM_LINK)
        sleep(3)