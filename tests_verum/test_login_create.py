import os
from selenium.webdriver.common.by import By
import time
import pytest
link = "https://dev.lie-detector.tech/"



class TestMainPage1():
    @pytest.mark.login
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        login = browser.find_element(By.CSS_SELECTOR, '[type~=text]')
        login.send_keys("admin")

        password = browser.find_element(By.CSS_SELECTOR, '[type~=password]')
        password.send_keys("verumP@1528word")

        button = browser.find_element(By.CLASS_NAME, 'button')
        button.click()
        browser.implicitly_wait(5)

    def go_to_main_page(self, browser):
        main_page_button = browser.find_element(By.CLASS_NAME, 'page-main__logo')
        main_page_button.click()

    def test_go_to_main_page(self, browser):
        browser.get(link)
        go_to_main_page(browser)

        print("finish test1")


