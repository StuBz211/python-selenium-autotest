from selenium.webdriver.common.by import By





class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_form > .btn-lg')

    REGISTER_USERNAME = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BTN = (By.CSS_SELECTOR, '#register_form > .btn-lg')


class ProductPageLocators:
    ADD_TO_CARD = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CARD = (By.CSS_SELECTOR, '.btn-cart')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    MESSAGES = (By.CSS_SELECTOR, "#messages")
