from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

TINDOG_URL = os.getenv('TINDOG_URL')
FACEBARK_EMAIL = os.getenv('FACEBARK_EMAIL')
FACEBARK_PASSWORD = os.getenv('FACEBARK_PASSWORD')

driver = webdriver.Chrome()
driver.get(TINDOG_URL)

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(1)
facebark_button = driver.find_element(By.CLASS_NAME, value='btn-facebark')
facebark_button.click()


# Switch to the Facebark popup window
sleep(2)
base_window = driver.window_handles[0]
facebark_window = driver.window_handles[1]
driver.switch_to.window(facebark_window)
print(driver.title)  # "Facebark"

# Fill in the form and submit
email = driver.find_element(By.ID, value='email')
password = driver.find_element(By.ID, value='pass')
email.send_keys(FACEBARK_EMAIL)
password.send_keys(FACEBARK_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to the Tindog window
sleep(2)
driver.switch_to.window(base_window)
print(driver.title)

# Allow location
sleep(2)
allow_location = driver.find_element(By.XPATH, value='//button[text()="Allow"]')
allow_location.click()

# Not interested in notifications
sleep(1)
not_interested = driver.find_element(By.XPATH, value='//button[text()="Not interested"]')
not_interested.click()

# Accept cookies
sleep(1)
accept_cookies = driver.find_element(By.XPATH, value='//button[text()="I Accept"]')
accept_cookies.click()

# Step 4 — like all 20 dogs
for n in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        # Match popup is in the way — dismiss it and continue
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        # Like button not loaded yet OR all dogs have been swiped — wait and retry
        sleep(2)


# # Target the main 'Like' heart button element
# like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
#
# while True:
#     try:
#         like_button.click()
#         sleep(1)  # 1-second delay between swipes to look human
#     except ElementClickInterceptedException:
#         # Catches cases where a "It's a Match!" screen pops up and blocks the like button
#         print("Match detected! Closing the match overlay popup...")
#         close_match = driver.find_element(By.CSS_SELECTOR, value='.match-popup a')
#         close_match.click()
#         sleep(1)
#     except NoSuchElementException:
#         # Handles cases where the button disappears because you ran out of daily swipes
#         print("Like button missing. Free tier swipe limits likely reached.")
#         break

driver.quit()