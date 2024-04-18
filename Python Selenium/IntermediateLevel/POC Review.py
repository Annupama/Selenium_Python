#from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

from DatePicker import DatePickerAutomation
from DriverClass import WebDriverFactory
# service_obj=Service()


class addProject:
    def __init__(self):
        # Create an instance of WebDriverFactory
        self.driver_factory = WebDriverFactory()
        self.driver = self.driver_factory.get_driver()

    def get(self):
        self.driver.get("https://chorusqa.cogninelabs.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("chorus.automation@cognine.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Welcome2Cognine")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
        self.driver.implicitly_wait(20)
        time.sleep(5)
        # driver.find_element(By.XPATH,"//input[@id='6']").click()
        self.driver.find_element(By.CSS_SELECTOR, "img[alt='Project Management']").click()
        time.sleep(3)
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("contentFrame")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Project']").click()
        time.sleep(3)
        # Adding new project in Project Management

        clientName = self.driver.find_element(By.XPATH, "//input[@type='text']")
        clientName.send_keys("client 1")
        time.sleep(3)
        client = self.driver.find_element(By.CSS_SELECTOR,
                                     "mat-option[class='mat-option mat-focus-indicator ng-star-inserted'] span")
        action = ActionChains(self.driver)
        action.move_to_element(client).click().perform()
        time.sleep(5)
        projectName = (self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Project Name']"))
        projectName.send_keys("Test Automate")
        time.sleep(3)
        testDescription = (self.driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Description']"))
        testDescription.send_keys("Test")
        time.sleep(3)
        notes = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Notes']")
        notes.send_keys("Testing")
        email = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
        email.send_keys("test.automate@cognine.com")
        time.sleep(3)
        DatePicker = DatePickerAutomation()
        time.sleep(3)
        date_to_select = '15-Apr-2024'
        DatePicker.select_date(date_to_select)
        time.sleep(3)
        print("click on button")


if __name__ == "__main__":
    project = addProject()
    project.get()







# pmo = driver.find_element(By.XPATH,"//span[normalize-space()='Select PMO']")
# action.move_to_element(pmo).click().perform()
# Techstack = driver.find_element(By.XPATH,"//span[@class='ng-star-inserted']")
# action.move_to_element(Techstack).click().perform()
# select = Select(element)
# Select.select_by_visible_text("text")
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# for checkbox in checkboxes:
#     driver.find_element(By.XPATH, )
#     if checkbox.get_attribute("value") == "Anirudh Lakshmipuram":
#         time.sleep(3)
#         checkbox.click()




