from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

#Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

#Navigate to website
driver.get('https://appbrewery.github.io/fake-newsletter-signup/')

#Find form input fields
fName = driver.find_element(By.NAME, 'fName')
lName = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')

#Fill out the form
fName.send_keys('Samuel')
lName.send_keys('Siyanbola')
email.send_keys('sammy@gmail.com')

#Locate sign-up button and click on it
button = driver.find_element(By.XPATH, '//*[@id="signup-form"]/button')
button.click()

# driver.quit()