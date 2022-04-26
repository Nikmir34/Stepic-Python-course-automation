from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_page_not_contains_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PAGE_HAVE_PRODUCT), "Basket contains product"

    def text_empty_basket_on_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Basket page is not empty"
