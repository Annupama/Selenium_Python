from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome_driver - Chrome browser
x = 5
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# ID, xpath, CSS selector, class name, name, linkText
#   xpath - //tagname[@attribute='value']
# CSS - tagname[attribute='value'], #id, .classname
# driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.NAME, "login-button").click()
sleep(x)
dropdown = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
sleep(x)
#dropdown.select_by_visible_text("Price (high to low)")
dropdown.select_by_index(3)
sleep(x)










