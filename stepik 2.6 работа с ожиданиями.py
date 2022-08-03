from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # говорим Selenium проверять в течение 13 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, 'book').click()
    number = browser.find_element(By.ID, 'input_value').text
    y = calc(number)
    print(y)
    browser.find_element(By.ID, 'answer').send_keys(y)
    submit = browser.find_element(By.ID, 'solve').click()
    time.sleep(3000)

finally:
# закрываем браузер после всех манипуляций
    browser.quit()
