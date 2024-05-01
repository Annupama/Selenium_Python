#from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from DriverClass import WebDriverFactory
import ProjectModule as pm


class addProject:
    def __init__(self):
        # Create an instance of WebDriverFactory
        self.driver_factory = WebDriverFactory()
        self.driver = self.driver_factory.get_driver()

    def get(self):
        self.driver.get(pm.login["url"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        time.sleep(3)

        self.driver.find_element(By.XPATH, pm.f_xpath["email"]).send_keys(pm.login["email"])
        time.sleep(2)
        self.driver.find_element(By.XPATH, pm.f_xpath["Submit"]).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, pm.f_xpath["password"]).send_keys(pm.login["password"])
        time.sleep(3)
        self.driver.find_element(By.XPATH, pm.f_xpath["SignIn"]).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, pm.f_xpath["yes"]).click()
        self.driver.implicitly_wait(20)
        time.sleep(5)
        # driver.find_element(By.XPATH,"//input[@id='6']").click()
        self.driver.find_element(By.CSS_SELECTOR, pm.f_xpath["pmicon"]).click()
        time.sleep(3)
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("undefined")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, pm.f_xpath["addproject"]).click()
        time.sleep(3)
        # Adding new project in Project Management
        wait = WebDriverWait(self.driver, 10)
        clientName = self.driver.find_element(By.XPATH, pm.f_xpath["clientName"])
        clientName.send_keys(pm.Proj1["clientName"])
        time.sleep(3)
        client = self.driver.find_element(By.CSS_SELECTOR, pm.f_xpath["client"])
        action = ActionChains(self.driver)
        action.move_to_element(client).click().perform()
        time.sleep(5)
        projectName = (self.driver.find_element(By.XPATH, pm.f_xpath["projectName"]))
        projectName.send_keys(pm.Proj1["projectName"])
        time.sleep(3)
        testDescription = (self.driver.find_element(By.XPATH, pm.f_xpath["testDescription"]))
        testDescription.send_keys(pm.Proj1["testDescription"])
        time.sleep(3)
        notes = self.driver.find_element(By.XPATH, pm.f_xpath["notes"])
        notes.send_keys(pm.Proj1["notes"])
        email = self.driver.find_element(By.XPATH, pm.f_xpath["emailid"])
        email.send_keys(pm.Proj1["email"])
        time.sleep(3)
        pmoelement = self.driver.find_element(By.XPATH, pm.f_xpath["pmod"])
        pmoelement.click()
        pmo = ["Divya Bandaru", "Pravallika Kanaparthi"]
        for option in pmo:
            label = self.driver.find_element(By.XPATH, pm.f_xpath["pmos"].format(option))
            label.click()
        time.sleep(3)
        body1 = self.driver.find_element(By.XPATH, "//body")
        action.move_to_element(body1).click().perform()
        dropdown_element = self.driver.find_element(By.XPATH, pm.f_xpath["technologiesd"])
        dropdown_element.click()
        technologies = [".Net", "Angular"]
        for option in technologies:
            label = self.driver.find_element(By.XPATH, pm.f_xpath["technologiess"].format(option))
            label.click()
        time.sleep(3)
        body = self.driver.find_element(By.XPATH, "//body")
        action.move_to_element(body).click().perform()
        time.sleep(3)
        # Start Date
        startdate = wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         "//mat-datepicker-toggle[@class ='mat-datepicker-toggle ng-tns-c53-1']//span[@class='mat-button-wrapper']//*[name()='svg']"))

        )
        startdate.click()
        time.sleep(5)
        date_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='May 2, 2024']")))
        # "//button[@class='mat-calendar-body-cell mat-calendar-body-active' and @aria-label='May 2, 2024']")))
        date_to_select.click()
        time.sleep(5)
        # End Date
        end_date = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                     "//mat-datepicker-toggle[@class ='mat-datepicker-toggle ng-tns-c53-2']//span[@class='mat-button-wrapper']//*[name()='svg']")))

        end_date.click()
        end_date_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='May 25, 2024']")))
                                                                 #"//button[@class='mat-calendar-body-cell' and @aria-label='May 25, 2024']")))
        end_date_select.click()
        file_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='Choose File']")))
        file_input.click()
        self.driver.execute_script("arguments[0].value = arguments[1]", file_input, pm.login["filepath"])
        time.sleep(5)
        add = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        add.click()


        # DatePicker = DatePickerAutomation()
        # time.sleep(3)
        # date_to_select = '15-Apr-2024'
        # DatePicker.select_date(date_to_select)
        # time.sleep(3)
        # print("click on button")


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




