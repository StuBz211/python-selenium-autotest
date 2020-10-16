from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.'


def test_add_to_card_button(browser):
    browser.get(TEST_URL)

    btn = WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")),
        message='Button not found'
    )
    assert btn
