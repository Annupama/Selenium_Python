#from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# service_obj=Service()
driver = webdriver.Chrome()
driver.get("https://chorusqa.cogninelabs.com/")
driver.maximize_window()
driver.implicitly_wait(2)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("chorus.automation@cognine.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Welcome2Cognine")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='idSIButton9']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='idSIButton9']").click()
driver.implicitly_wait(20)
time.sleep(5)
#driver.find_element(By.XPATH,"//input[@id='6']").click()
driver.find_element(By.CSS_SELECTOR,"img[alt='Project Management']").click()
time.sleep(3)
driver.implicitly_wait(2)
driver.switch_to.frame("contentFrame")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//button[normalize-space()='Add Project']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("AutomateTest")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@formcontrolname='projectName']").send_keys("POCReview")
time.sleep(2)

print("click on button")
