import pytest

from pages.product_page import ProductPage


base_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.parametrize('link', [
    f"{base_url}?promo=offer0",
    f"{base_url}?promo=offer1",
    f"{base_url}?promo=offer2",
    f"{base_url}?promo=offer3",
    f"{base_url}?promo=offer4",
    f"{base_url}?promo=offer5",
    f"{base_url}?promo=offer6",
    pytest.param(f"{base_url}?promo=offer7", marks=pytest.mark.xfail),
    f"{base_url}?promo=offer8",
    f"{base_url}?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.is_book_added()
