import time


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from DriverClass import WebDriverFactory


class DatePickerAutomation:

    def __init__(self):
        # Create an instance of WebDriverFactory
        self.driver_factory = WebDriverFactory()
        self.driver = self.driver_factory.get_driver()

    def select_date(self, date):
        print("test")
        time.sleep(3)
        date_picker_icon = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//mat-datepicker-toggle[@class='mat-datepicker-toggle ng-tns-c50-1']//span[@class='mat-button-wrapper']//*[name()='svg']"))
        )
        date_picker_icon.click()
        date_picker = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "mat-calendar"))
        )
        date_element = self.driver.find_element(By.XPATH,"//td[@data-mat-row='1']/button[@type='button']")
        date_element.click()
