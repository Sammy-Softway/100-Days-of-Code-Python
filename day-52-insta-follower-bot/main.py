import os
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

load_dotenv()

NAAN_EMAIL = os.getenv('NAAN_EMAIL')
NAAN_PASSWORD = os.getenv('NAAN_PASSWORD')
NAAN_URL = os.getenv('NAAN_URL')
SIMILAR_ACCOUNT = os.getenv('SIMILAR_ACCOUNT')

class InstaFollower:
    def __init__(self):
        # Initialize Chrome options to keep browser open or block notifications
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options)

    def login(self):
        self.driver.get(NAAN_URL)
        sleep(2)

        # If a cookie banner is present, dismiss it (Share-a-Naan doesn't show one,
        # but this is here so the same code works against the real site too).
        decline = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Decline')]")
        if decline:
            decline[0].click()

        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(NAAN_EMAIL)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(NAAN_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        # Dismiss "Save your login info?" → "Not now"
        save_info = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_info:
            save_info[0].click()
        sleep(1)

        # Dismiss "Turn on notifications" → "Not Now"
        notifications = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if notifications:
            notifications[0].click()

    def find_followers(self):
        search_icon = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Search')]")
        search_icon.click()
        sleep(2)

        search_input = self.driver.find_element(By.CLASS_NAME, 'naan-search-input')
        search_input.send_keys(SIMILAR_ACCOUNT)
        search_input.send_keys(Keys.ENTER)
        sleep(2)

        followers_link = self.driver.find_element(By.CLASS_NAME, "naan-followers-link")
        followers_link.click()

        # The scrollable element inside the followers dialog. Inspect to confirm the class.
        modal = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll")
        for _ in range(10):
            # "scroll this element to the bottom" → loads the next batch of followers
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(1)



    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.followers-scroll button')

        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                # An "Unfollow?" dialog opened (you already follow this account).
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()