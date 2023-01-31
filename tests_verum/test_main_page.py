from automation_VERUM.pages.login_page import LoginPage
from automation_VERUM.pages.new_test_page import NewTest
from automation_VERUM.pages.main_page import MainPage
import time
import pytest

@pytest.mark.login_guest
class LoginFromMainPage():
    @pytest.fixture(scope='class', autouse=True)
    def test_guest_can_go_to_login_page(self, browser):
        link = "https://dev.lie-detector.tech/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()                      # открываем страницу
        login_page = LoginPage(browser, browser.current_url)    # выполняем метод страницы — переходим на страницу логина
        main_page = page.go_to_login_page()
        login_page_assertions = LoginPage(browser, link)  # инициализируем объект из класса LoginPage
        login_page_assertions.should_be_login_url  # проверяем что в текущем урле есть строка "tech"
        login_page_assertions.should_be_login_form  # проверяем что на странице есть форма, в которой можно ввети логин и пароль
        time.sleep(2)
        #return login_page.should_be_login_page()

class TestLoginFromMainPage(LoginFromMainPage):

    def test_guest_should_see_globe_page(self, browser):
        link = "https://dev.lie-detector.tech/"
        page = MainPage(browser, link)
        page.should_see_globe_page()


    def test_open_new_test(self, browser):
        link = "https://dev.lie-detector.tech/"
        link_new_test = 'https://dev.lie-detector.tech/test/new'
        page = MainPage(browser, link)
        page.open_new_test()
        page_test = NewTest(browser, link_new_test)
        page_test.insert_test_name()


        time.sleep(5)
