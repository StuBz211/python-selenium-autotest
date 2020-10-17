import random
import time

import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


base_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
links = [f"{base_url}?promo=offer{i}" for i in range(10)]

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)  # для каждого теста, запускается без вызова
    def setup(self, browser):
        email = str(random.randint(750000, 4500000)) + "@mail.ru"
        password = str(time.time())

        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_card()
        page.is_book_added()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.add_to_card()
    page.is_book_added()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART)


def test_message_disappeared_after_adding_product_to_basket( browser):
    page = ProductPage(browser, product_link)
    page.open()
    assert page.is_disappeared(*ProductPageLocators.ALERT_ADDED_TO_CART)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    basket_page = page.go_to_basket()
    basket_page.basket_should_by_empty()
    basket_page.basket_should_by_empty_msg()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
