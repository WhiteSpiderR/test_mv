from src.ui.pages.main_page import MainPage


class MainPageKeywords:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)

    def start_registration(self, email):
        self.main_page.fill_registration_email_field(email)
        self.main_page.select_registration_status()
