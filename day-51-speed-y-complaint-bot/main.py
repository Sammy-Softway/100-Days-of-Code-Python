from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 24
PROMISED_UP = 13
SPEED_TEST_URL = os.getenv('SPEED_TEST_URL')
Y_LOGIN_URL = os.getenv("Y_LOGIN_URL")
Y_EMAIL = os.getenv("Y_EMAIL")
Y_PASSWORD = os.getenv("Y_PASSWORD")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        # accept_button = self.driver.find_element(By.ID, value="#onetrust-accept-btn-handler")
        # accept_button.click()

        sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value="button")
        go_button.click()

        sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3').text

        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)
        sleep(2)

        self.driver.find_element(By.NAME, value="username").send_keys(Y_EMAIL)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(Y_PASSWORD)
        password.send_keys(Keys.ENTER)

        sleep(3)
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR, value='div[aria-label="Post text"]')
        tweet = f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        tweet_compose.send_keys(tweet)

        sleep(2)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, value='.x-compose-form button')
        tweet_button.click()

        sleep(2)
        self.driver.quit()

y_bot = InternetSpeedTwitterBot()


y_bot.get_internet_speed()

y_bot.tweet_at_provider()