import pytest

from .base_page import BasePage
from selenium.webdriver.common.by import By
from automation_VERUM.locators import LoginPageLocators
import time


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


        #return LoginPage(browser=self.browser, url=self.browser.current_url)

       # alert = self.browser.switch_to.alert
        #alert.accept()


    def open_new_test(self):

        new_test = self.browser.find_element(*LoginPageLocators.NEW_TEST)
        new_test.click()
        time.sleep(3)






