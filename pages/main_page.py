from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainLocators

class MainPage(BasePage):

    def start_bnt_click(self):
        self.browser.execute_script("window.scrollBy(0, 600);")
        start_button = self.browser.find_element(*MainLocators.START_GAME_BNT)
        start_button.click()
        self.browser.execute_script("window.scrollBy(0, -300);")

    def close_cookies(self):
        close_button = self.browser.find_element(*MainLocators.CLOSE_COOKIES_BTN)
        close_button.click()
