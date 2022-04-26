from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_INPUT_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

class BooksPages():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary')
    ADD_TO_BASKET_NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.alertinner strong')
    ADD_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    VIEW_BASKET_BUTTON = (By.XPATH, "//a[text()='View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_PAGE_HAVE_PRODUCT = (By.CSS_SELECTOR, 'h2.col-sm-6')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')
