from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url # реализуйте проверку на корректный url адрес
        assert login_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)# реализуйте проверку, что есть форма логина


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)
        # реализуйте проверку, что есть форма регистрации на странице

    def generation_registration_data(self):
        return (str(time.time()) + "@fakemail.org", "SuperSTR0n%p1ssw0r#")

    def register_new_user(self, email, password):
        self.email = email
        self.password = password

        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_FORM).send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_FORM).send_keys(password)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_INPUT).send_keys(password)

        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()



