import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CLASS_NAME, "form-control")
    for element in elements:
        element.send_keys("ball")


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    print(file_path)
    attach = browser.find_element(By.ID, 'file').send_keys(file_path)
    submit = browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(10)

finally:
# закрываем браузер после всех манипуляций
    browser.quit()
