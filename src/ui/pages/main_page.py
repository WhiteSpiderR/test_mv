from src.ui.selenium_utils import SeleniumUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    registration_status_button = (
        By.XPATH, "//div[@class='RegistrationForm_selectCustomSh__2wu8i']")
    registration_email_field = (By.XPATH, "//div[@class='RegistrationForm_inputHolderSh__3TVsv']//input")
    registration_status_student = (
        By.XPATH, "//ul[@class='RegistrationForm_selectUl__3UgHC']//li/a[text()='Студент медицинского ВУЗа']")

    def __init__(self, driver):
        self.driver = driver

    def fill_registration_email_field(self, email):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.registration_email_field))
        element.clear()
        element.send_keys(email)

    def select_registration_status(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.registration_status_button)).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.registration_status_student))
        element.click()



