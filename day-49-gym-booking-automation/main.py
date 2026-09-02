from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
from dotenv import load_dotenv
import time


#--- BOOKING SUMMARY ---
classes_booked = 0
waitlists_joined = 0
already_booked_or_waitlisted = 0


# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

load_dotenv()
GYM_NAME = os.getenv("GYM_NAME")
GYM_EMAIL = os.getenv("GYM_EMAIL")
GYM_PASSWORD = os.getenv("GYM_PASSWORD")
GYM_URL = os.getenv("GYM_URL")

chrome_options = webdriver.ChromeOptions()

# Keep the browser open if the script finishes or crashes.
# If True, you need to *manually* QUIT Chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)

# Create a folder for the Chrome Profile Selenium will use every time
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# include double -- for command line argument to Chrome
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

#Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

#Navigate to website
driver.get(GYM_URL)

# Alternative to using time.sleep(): use a standalone wait object
wait = WebDriverWait(driver, 5)

# ---------------- Step 9: Network Resilience Defined functions ----------------

# Simple retry wrapper
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)


# Function to perform entire login process with retry
def login():
    # Click login button to go to login page
    login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    # Fill in login form
    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(GYM_EMAIL)

    password_input = driver.find_element(By.ID, 'password-input')
    password_input.clear()
    password_input.send_keys(GYM_PASSWORD)

    submit_button = driver.find_element(By.ID, 'submit-button')
    submit_button.click()

    # Wait for schedule page to load
    wait.until(ec.presence_of_element_located((By.ID, 'schedule-page')))

def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked" or booking_button.text == "Waitlisted")

def get_my_bookings():
    # Navigate to My Bookings page
    my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
    my_bookings_link.click()

    # Wait for My Bookings page to load
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

# ----------------  Step 2 - Automated Login ----------------

# # Click login button to go to login page
# login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
# login_button.click()
#
# #Fill in login form
# email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
# email_input.clear()
# email_input.send_keys(GYM_EMAIL)
#
# password_input = driver.find_element(By.ID, 'password-input')
# password_input.clear()
# password_input.send_keys(GYM_PASSWORD)
#
# submit_button = driver.find_element(By.ID, 'submit-button')
# submit_button.click()
#
# # Wait for schedule page to load
# wait.until(ec.presence_of_element_located((By.ID, 'schedule-page')))


# Using the retry and login function together
retry(login, description="login")



# ----------------  Step 3 - Class Booking: Book Upcoming Class  ----------------

schedule_day_Group = driver.find_elements(By.CLASS_NAME, 'Schedule_dayGroup__y79__')
# print(schedule_day_Group)

for schedule in schedule_day_Group:
    fittness_class_day = schedule.find_element(By.CLASS_NAME, 'Schedule_dayTitle__YBybs').text
    # print(fittness_class_day)

    if "Tue" in fittness_class_day or "Thu" in fittness_class_day:
        tue_or_thur_classes = schedule.find_elements(By.CLASS_NAME, 'ClassCard_cardHeader__D9pf3')

        for fittness_class in tue_or_thur_classes:
            fittness_class_time = fittness_class.find_element(By.CSS_SELECTOR, "p[id^='class-time-").text

            if "6:00 PM" in fittness_class_time:
                fittness_class_name = fittness_class.find_element(By.CSS_SELECTOR, 'h3[id^="class-name-"]').text

                button = fittness_class.find_element(By.CSS_SELECTOR, 'button[id^="book-button-"]')

                if button.text == "Booked":
                    print(f"Already booked: {fittness_class_name} for {fittness_class_day}, {fittness_class_time}")
                    already_booked_or_waitlisted += 1
                elif button.text == "Waitlisted":
                    print(f"Already on waitlist: {fittness_class_name} for {fittness_class_day}, {fittness_class_time}")
                    already_booked_or_waitlisted += 1
                elif button.text == "Book Class":
                    # Using the retry and book_class function together
                    retry(lambda: book_class(button), description="book class")
                    classes_booked += 1
                    print(f"Successfully booked: {fittness_class_name} for {fittness_class_day}, {fittness_class_time}")
                    time.sleep(0.5)
                elif button.text == "Join Waitlist":
                    # Using the retry and book_class function together
                    retry(lambda: book_class(button), description="book class")
                    waitlists_joined += 1
                    print(f"Joined waitlist for: {fittness_class_name} for {fittness_class_day}, {fittness_class_time}")
                    time.sleep(0.5)


# total_6pm_classes_processed = classes_booked + waitlists_joined + already_booked_or_waitlisted
# # Print summary
# print("\n--- BOOKING SUMMARY ---")
# print(f"Classes Booked: {classes_booked}\n"
#       f"Waitlist Joined: {waitlists_joined}\n"
#       f"Already Booked or Waitlisted: {already_booked_or_waitlisted}\n"
#       f"Total Tuesday & Thursday 6pm Classes Processed: {total_6pm_classes_processed}")

# ----------------  Step 7: Verify Class Bookings on My Bookings Page ----------------

total_6pm_classes_processed = classes_booked + waitlists_joined + already_booked_or_waitlisted
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_6pm_classes_processed} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# # Navigate to My Bookings page
# my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
# my_bookings_link.click()
#
# # Wait for My Bookings page to load
# wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

# Using the retry and get_my_bookings function together
retry(get_my_bookings, description="get my bookings page")

# Count all Tuesday/Thursday 6pm bookings
verified_count = 0

# Find ALL booking cards (both confirmed and waitlist)
booking_card = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-booking_']")
waitlist_card = driver.find_elements(By.CSS_SELECTOR, "div[id^='waitlist-card-waitlist_']")
confirm_cards = booking_card + waitlist_card

for card in confirm_cards:
    try:
        booked_wait_day = card.find_element(By.CSS_SELECTOR, "p").text
        # Check if it's a Tuesday or Thursday 6pm class
        if ("Tue" in booked_wait_day or "Thu" in booked_wait_day) and "6:00 PM" in booked_wait_day:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "Booked or Waitlist Class:" text found (not a booking card)
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_6pm_classes_processed} bookings")
print(f"Found: {verified_count} bookings")

if total_6pm_classes_processed == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_6pm_classes_processed - verified_count} bookings")


# driver.quit()