from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from automation_VERUM.locators import LoginPageLocators
from automation_VERUM.locators import GlobePageLocators
import time

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what): # проверка на отсутствие ошибки NoSuchElementException
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def go_to_login_page(self):
        login = self.browser.find_element(*LoginPageLocators.NAME_LOGIN)
        login.send_keys("admin")
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("verumP@1528word")
        button = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN)
        button.click()


    def should_be_login_link(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_see_globe_page(self):
        assert self.is_element_present(*GlobePageLocators.MAIN_BUTTON_LOGO), "Logo element is not presented"


    def element_is_visible(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))
        #assert self.elements_are_present(locator)

    def element_is_not_visible(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.browser.execute_script("argument[0].scrollIntoView();", element)


