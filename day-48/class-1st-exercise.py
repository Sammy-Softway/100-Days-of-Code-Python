from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

#Navigate to website
driver.get("https://www.python.org/")


#--------------------------My Solution style----------------------------#
# menu = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# # print(menu.find_elements(By.CSS_SELECTOR, 'li'))
#
# menu_list = menu.find_elements(By.CSS_SELECTOR, 'li')
# # print(menu_list)
# # print(menu_list[0].text)
#
# menu_dict = {
#     index: {
#         'time': event.find_element(By.CSS_SELECTOR, 'time').text,
#         'name': event.find_element(By.CSS_SELECTOR, 'a').text,
#     }
#     for index in range(len(menu_list))
#     for (index, event) in enumerate(menu_list)
# }
# pprint(menu_dict)

#--------------------------Dr Angela's Solution style----------------------------#
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }
pprint(events)

driver.quit()