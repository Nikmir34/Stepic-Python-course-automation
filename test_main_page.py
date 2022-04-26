from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

def test_url_should_be_have_login_url(browser):
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser,link)
    page.open()
    page.should_be_login_url()

def test_login_page_should_be_login_form(browser):
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_login_page_should_be_register_form(browser):
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_page_not_contains_product()
    page.text_empty_basket_on_basket_page()


