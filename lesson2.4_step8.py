from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price_house = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")
                                            )
    button = browser.find_element_by_id('book')
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_id('answer')
    field.send_keys(y)

    button = browser.find_element_by_id('solve')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)

    print(browser.switch_to.alert.text)

    # закрываем браузер после всех манипуляций
    browser.quit()