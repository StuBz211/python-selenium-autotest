from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        btn = self.get_element(ProductPageLocators.ADD_TO_CARD)
        btn.click()

    def is_book_added(self):
        book_name = self.get_element(ProductPageLocators.PRODUCT_NAME).text
        added_to_cart_msg = self.get_element(ProductPageLocators.ALERT_ADDED_TO_CART).text
        assert book_name in added_to_cart_msg, 'book name not in messages'

        book_price = self.get_element(ProductPageLocators.PRODUCT_PRICE).text
        cart_status = self.get_element(ProductPageLocators.ALERT_CART_STATUS).text
        assert book_price in cart_status, 'book price not in card'

