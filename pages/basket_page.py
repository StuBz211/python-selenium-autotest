from .base_page import BasePage
from .locators import BasketLocator


class BasketPage(BasePage):
    def is_basket_empty(self):
        self.is_element_present(*BasketLocator.BASKET_ITEMS)

    def has_empty_basket_msg(self):
        msg = self.get_element(*BasketLocator.BASKET_MSG).text
        assert 'Ваша корзина пуста' in msg
