import pytest

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


base_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
links = [f"{base_url}?promo=offer{i}" for i in range(10)]

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.is_book_added()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_card()
    assert not page.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART)


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    assert not page.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART)


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    assert not page.is_disappeared(*ProductPageLocators.ALERT_ADDED_TO_CART)

