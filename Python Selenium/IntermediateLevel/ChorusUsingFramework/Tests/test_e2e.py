import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


# @pytest.mark.usefixtures("setup")


class TestOne(BaseClass):
    def test_e2e(self, setup):
        pm_icon = setup.driver.find_element(By.CSS_SELECTOR, "img[alt='Project Management']")
        pm_icon.click()
        setup.driver.implicitly_wait(2)
        setup.driver.switch_to.frame("undefined")
        setup.driver.implicitly_wait(5)


