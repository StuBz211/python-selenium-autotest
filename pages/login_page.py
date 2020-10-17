from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'is not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Not login username field"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Not login password field"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Not login button"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_USERNAME), "Not login username field"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_1), "Not login password 1 field "
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_2), "Not login password 2 field "
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), "Not register button"
