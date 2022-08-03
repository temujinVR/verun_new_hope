from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    treasure = browser.find_element(By.ID, 'treasure')
    val = treasure.get_attribute('valuex')
    y = calc(val)
    print(y)
    sol = browser.find_element(By.ID, "answer").send_keys(y)
    check_box = browser.find_element(By.ID, "robotCheckbox").click()
    round = browser.find_element(By.ID, 'robotsRule').click()
    submit = browser.find_element(By.CLASS_NAME, 'btn').click()



    time.sleep(10)

finally:
# закрываем браузер после всех манипуляций
    browser.quit()

