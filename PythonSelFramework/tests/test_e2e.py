import pytest
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        pm_icon = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Project Management']")
        pm_icon.click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("undefined")
        self.driver.implicitly_wait(5)