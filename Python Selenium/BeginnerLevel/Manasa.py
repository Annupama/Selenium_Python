import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


def browser():
    driver = webdriver.Chrome()
    driver.get("https://portal.synchrogistics.com")
    print("Login Successful")

    def login():
        nonlocal driver  # Using nonlocal to modify the driver variable from the browser function
        driver.minimize_window()
        driver.implicitly_wait(10)
        driver.maximize_window()
        try:
            Okay = driver.find_element(By.XPATH, "//button[normalize-space()='Okay']")
            Okay.click()
        except NoSuchElementException:
            driver.implicitly_wait(5)
            driver.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
            driver.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print("Login Successful")
            driver.implicitly_wait(5)
            print(driver.title)

    def close_browser():
        nonlocal driver  # Using nonlocal to modify the driver variable from the browser function
        driver.quit()

    return login, close_browser