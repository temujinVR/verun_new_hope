from selenium.webdriver.common.by import By


class LoginPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    NAME_LOGIN = (By.CSS_SELECTOR, '[type~=text]')
    PASSWORD = (By.CSS_SELECTOR, '[type~=password]')
    BUTTON_LOGIN = (By.CLASS_NAME, 'button')
    LOGIN_FORM = (By.CLASS_NAME, 'template-auth__page')
    NEW_TEST = (By.CSS_SELECTOR, '[href$="test/new"]')

class NewTestPageLocators():
    TEST_NAME = (By.CSS_SELECTOR, '[class$=test__name__input]')
    SAVE_TEST = (By.CSS_SELECTOR, "[class$=button-blue]")
    All_TYPE_QUESTIONS_LIST = (By.CLASS_NAME, "test__category")
    O_TYPE_QUESTION = (By.CLASS_NAME, 'test__category')

class GlobePageLocators():
    MAIN_BUTTON_LOGO = (By.CLASS_NAME, 'page-main__logo')


