from .base_page import BasePage
from .locators import BasketLocator


class BasketPage(BasePage):
    def basket_should_by_empty(self):
        assert self.is_not_element_present(*BasketLocator.BASKET_ITEMS)

    def basket_should_by_empty_msg(self):
        msg = self.get_element(*BasketLocator.BASKET_MSG).text
        assert 'Ваша корзина пуста' in msg
