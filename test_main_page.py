from .pages import MainPage

base_url = "http://selenium1py.pythonanywhere.com"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, base_url)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, base_url)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, base_url)
    basket_page = page.go_to_basket()
    assert basket_page.is_basket_empty()
    assert basket_page.has_empty_basket_msg()
