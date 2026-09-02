from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

#Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

#Navigate to website
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# number_of_wiki_articles = driver.find_element(By.XPATH, '//*[@id="mwDw"]')
number_of_wiki_articles = driver.find_element(By.CSS_SELECTOR, '#mwDw')
# print(number_of_wiki_articles.text)
#
# driver.quit()

#Click effect
# number_of_wiki_articles.click()

#Find element by Link Text
search = driver.find_element(By.NAME, 'search')

#Sending keyboard input to Selenium
search.send_keys('python', Keys.ENTER)