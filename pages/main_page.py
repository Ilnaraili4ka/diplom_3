import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators



class MainPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Нажать на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.main_page_loading_wait()
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_profile_button(self):
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)

    @allure.step("Нажать на кнопку 'Лента заказов'")
    def click_feed_button(self):
        self.main_page_loading_wait()
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step("Нажать на логотип Stellar Burgers")
    def click_logo(self):
        self.click_on_element(MainPageLocators.LOGO)

    @allure.step("Проверить, что текущая страница — Лента заказов")
    def is_on_feed_page(self):
        return self.current_url()

    @allure.step("Проверить, что текущая страница — главная")
    def is_on_main_page(self):
        return self.current_url()


