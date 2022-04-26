from .base_page import BasePage
from .locators import BooksPages


class ShellcoderbookPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*BooksPages.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*BooksPages.ADD_TO_BASKET_NAME_OF_PRODUCT), (
            "Message about adding is not presented")
        message = self.browser.find_element(*BooksPages.ADD_TO_BASKET_NAME_OF_PRODUCT).text
        product_name = self.browser.find_element(*BooksPages.PRODUCT_NAME).text
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*BooksPages.PRICE_MESSAGE), (
            "Message basket total is not presented")
        price_message = self.browser.find_element(*BooksPages.PRICE_MESSAGE).text
        product_price = self.browser.find_element(*BooksPages.BOOK_PRICE).text
        assert product_price in price_message, ("No product price in the message")

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*BooksPages.ADD_TO_BASKET_SUCCESS_MESSAGE), \
            ("Meassage about success adding product to basket is presented")

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*BooksPages.ADD_TO_BASKET_SUCCESS_MESSAGE), \
            ("Meassage about success adding product to basket is not disappeared")









