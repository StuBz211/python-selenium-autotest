import pytest
from .pages import MainPage


base_url = "http://selenium1py.pythonanywhere.com/"


class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, base_url)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, base_url)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, base_url)
        page.open()
        basket_page = page.go_to_basket()
        basket_page.basket_should_by_empty()
        basket_page.basket_should_by_empty_msg()
