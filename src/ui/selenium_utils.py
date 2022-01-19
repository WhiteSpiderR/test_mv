from selenium import webdriver
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WEBDRIVER_PATH = os.path.join(ROOT_DIR, 'webdriver')


class SeleniumUtils:

    def driver(self):
        """
        selenium driver
        :return:
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        print(WEBDRIVER_PATH)
        driver = webdriver.Chrome(f"{WEBDRIVER_PATH}/chromedriver.exe", chrome_options=chrome_options)
        return driver

    def get_site(self, driver, url):
        driver.get(url)
