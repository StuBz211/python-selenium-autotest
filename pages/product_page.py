from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD)
        btn.click()

    def get_messages(self):
        message_el = self.browser.find_element(*ProductPageLocators.MESSAGES)
        assert message_el, 'Messages not found'
        return message_el

    def is_book_added(self):
        book_name_el = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert book_name_el, 'book name element not found'
        book_name = book_name_el.text
        message = self.get_messages().text
        assert 'был добавлен в вашу корзину.' in message
        assert book_name in message, 'book name not in messages'

        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert book_price, 'can\'t find book price'
        assert book_price.text in message, 'book price not in card'

