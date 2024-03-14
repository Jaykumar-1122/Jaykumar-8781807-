# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(8)

# Clicking on the best sellers link
best_sellers_link = driver.find_element("xpath", "/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[1]")
best_sellers_link.click()

# Waiting for the best sellers page to load
time.sleep(5)

# Finding the search bar and entering text
search_bar = driver.find_element("id", "twotabsearchtextbox")
search_bar.send_keys("headphones")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "headphones" in driver.title

# Selecting a headphone from the search results
headphone_link = driver.find_element("xpath", "//span[contains(@class, 'a-size-medium a-color-base a-text-normal')][1]")
headphone_link.click()

# Waiting for the headphone details page to load
time.sleep(2)

# Scrolling down to read product information
action = ActionChains(driver)
action.send_keys(Keys.PAGE_DOWN).perform()

# Waiting for 4 seconds after scrolling down
time.sleep(4)

# Locating the quantity dropdown
quantity_dropdown = Select(driver.find_element(By.NAME, "quantity"))

# Selecting the option for quantity 2
quantity_dropdown.select_by_value("2")

# Waiting for 3 seconds after setting quantity to 2
time.sleep(3)

# Closing the webdriver
driver.close()
