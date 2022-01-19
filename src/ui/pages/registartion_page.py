from src.ui.selenium_utils import SeleniumUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os


class RegistrationPage:

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_REG_PATH = f"{os.path.join(ROOT_DIR, 'document_registartion')}/logo-mobile.png"

    name_field = (By.XPATH, "//input[@name='firstName']")
    surname_field = (By.XPATH, "//input[@name='lastName']")
    patronymic_field = (By.XPATH, "//input[@name='middleName']")
    country_field_list = (By.XPATH, "//div[@class='open-select-box open']//input[@name='country']/..//div[@class='']/input")
    region_field_list = (By.XPATH, "//div[@class='open-select-box open']//input[@name='region']/..//div[@class='']/input")
    university_field_list = (By.XPATH, "//div[@class='open-select-box open']//input[@name='university']/..//div[@class='']/input")
    issue_year_field_list = (By.XPATH, "//div[@class='open-select-box open']//input[@name='finishDate']/..//div[@class='']/input")

    def __init__(self, driver):
        self.driver = driver

    def fill_name_field(self, name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.name_field))
        element.clear()
        element.send_keys(name)

    def fill_surname_field(self, surname):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.surname_field))
        element.clear()
        element.send_keys(surname)

    def fill_patronymic_field(self, patronymic):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.patronymic_field))
        element.clear()
        element.send_keys(patronymic)

    def select_country(self, country):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.country_field_list))
        element.send_keys(country)
        element.send_keys(Keys.RETURN)

    def select_region(self, region):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.region_field_list))
        element.send_keys(region)
        element.send_keys(Keys.RETURN)

    def select_university(self, university):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.university_field_list))
        element.send_keys(university)
        element.send_keys(Keys.RETURN)

    def select_issue_year(self, issue_year):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.issue_year_field_list)) 
        element.send_keys(issue_year)
        element.send_keys(Keys.RETURN)

    def download_document(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.issue_year_field_list))
        element.send_keys(self.FILE_REG_PATH)

    def click_registration_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.issue_year_field_list))
        element.send_keys(self.FILE_REG_PATH)
