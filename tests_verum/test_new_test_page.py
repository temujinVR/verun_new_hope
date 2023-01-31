from automation_VERUM.pages.login_page import LoginPage
from automation_VERUM.pages.new_test_page import NewTest
from automation_VERUM.pages.main_page import MainPage
from .test_main_page import LoginFromMainPage
import time
import pytest

@pytest.mark.login_guest
class TestNewTestFromMainPage(LoginFromMainPage):

    def test_new_test(self, browser):
        link = "https://dev.lie-detector.tech/test/new"
        smash_buttons = NewTest(browser, link)
        smash_buttons.open()
        smash_buttons.insert_test_name()
        #smash_buttons.add_all_type_questions()
        smash_buttons.get_all_type_questions()
        time.sleep(3)
        #smash_buttons.save_test()

        time.sleep(3)
