from automation_VERUM.pages.main_page import MainPage
from automation_VERUM.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from automation_VERUM.locators import NewTestPageLocators


class NewTest(BasePage):

    def insert_test_name(self):
        new_test_name = self.browser.find_element(*NewTestPageLocators.TEST_NAME)
        new_test_name.send_keys('test ')

    def save_test(self):
        save_button = self.browser.find_element(*NewTestPageLocators.SAVE_TEST)
        save_button.click()

    def add_all_type_questions(self):
        O_type = self.browser.find_element(*NewTestPageLocators.O_TYPE_QUESTION)
        print(O_type)

    def get_all_type_questions(self):
        checked_list = self.elements_are_present(*NewTestPageLocators.All_TYPE_QUESTIONS_LIST)
        data = []
        for box in checked_list:
            print(box.text)


