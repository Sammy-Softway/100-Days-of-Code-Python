from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# # --- NEW: Anti-bot bypass configurations ---
# # 1. Disables the "Chrome is being controlled..." banner
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
#
# # 2. Makes the browser look like a normal Windows user instead of a script
# chrome_options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36")
# # -------------------------------------------

#Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

#Navigate to website
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# Wait 3 seconds to let the page fully load before searching for elements
driver.implicitly_wait(3)

try:
    price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
    print(f"The price is ${price_dollar.text}.{price_cents.text}")
except Exception as e:
    print("Could not find the price. The bot-check page might still be appearing.")


#Used to close one active tab
# driver.close()
#Used to quite the entire program
driver.quit()