import allure
from pages.base_page import BasePage
from locators.auth_locators import AuthLocators
import time


class AuthPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.send_keys_to_input(AuthLocators.EMAIL, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.send_keys_to_input(AuthLocators.PASSWORD, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click_on_element(AuthLocators.LOGIN_BUTTON)

    @allure.step("Дождаться видимости формы авторизации")
    def wait_form_auth(self):
        self.wait_for_element(AuthLocators.LOGIN_BUTTON)

    @allure.step("Авторизация пользователя")
    def auth(self, password, email):
        self.wait_form_auth()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

