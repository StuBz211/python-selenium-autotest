import pytest

from pages.product_page import ProductPage


base_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
links = [f"{base_url}?promo=offer{i}" for i in range(10)]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.is_book_added()
