from pages.product_page import ShellcoderbookPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time
import pytest



@pytest.mark.product
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        self.browser = browser
        page = LoginPage(browser, link)
        page.open()
        email, password = page.generation_registration_data()
        page.register_new_user(email, password)

        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ShellcoderbookPage(browser, link)
        page.open()
        time.sleep(1)
        page.add_product_to_basket()
        time.sleep(2)
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ShellcoderbookPage(browser, link)
        page.open()
        page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ShellcoderbookPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_product_to_basket()
    time.sleep(2)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ShellcoderbookPage(browser, link)
    page.open()
    page.add_product_to_basket()
    time.sleep(2)
    page.guest_cant_see_success_message_after_adding_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ShellcoderbookPage(browser, link)
    page.open()
    page.add_product_to_basket()
    time.sleep(2)
    page.message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ShellcoderbookPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ShellcoderbookPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_page_not_contains_product()
    page.text_empty_basket_on_basket_page()



