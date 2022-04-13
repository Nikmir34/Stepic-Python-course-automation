from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('treasure')
    x_attribute = x_element.get_attribute('valuex')
    x = x_attribute
    y = calc(x)

    field = browser.find_element_by_id('answer')
    field.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobatton = browser.find_element_by_id('robotsRule')
    radiobatton.click()

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()