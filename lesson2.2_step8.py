from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Nikita')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Mironov')

    email = browser.find_element_by_name('email')
    email.send_keys('test@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_file.txt')

    file_button = browser.find_element_by_id('file')
    file_button.send_keys(file_path)

    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

