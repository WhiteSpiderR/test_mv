from src.ui.selenium_utils import SeleniumUtils
from src.ui.keywords.ui.main_page_keywords import MainPageKeywords
from src.ui.keywords.ui.registartion_page_keywords import RegistrationPageKeywords
from src.test_data.common_test_data import CommonTestData


class TestRegistration:

    def setup_class(self):
        self.driver = SeleniumUtils().driver()

    def test_registration(self):
        email = CommonTestData.email
        SeleniumUtils().get_site(self.driver, url='https://test.mirvracha.ru')
        MainPageKeywords(self.driver).start_registration(email=email)
        RegistrationPageKeywords(self.driver).fill_registration_form(
            name='Тест', surname='Тестовой', patronymic='Тестович', country='Российская Федерация', region="Москва",
            university='Московский гос. медико-стомат. университет', issue_year="2021")

    def teardown_class(self):
        self.driver.quit()
