from src.ui.pages.registartion_page import RegistrationPage


class RegistrationPageKeywords:

    def __init__(self, driver):
        self.driver = driver
        self.reg_page = RegistrationPage(self.driver)

    def fill_registration_form(self, name, surname, patronymic, country, region, university, issue_year):
        self.reg_page.fill_name_field(name)
        self.reg_page.fill_surname_field(surname)
        self.reg_page.fill_patronymic_field(patronymic)
        self.reg_page.select_country(country)
        self.reg_page.select_region(region)
        self.reg_page.select_university(university)
        self.reg_page.select_issue_year(issue_year)
        self.reg_page.download_document()

