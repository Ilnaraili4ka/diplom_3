import allure

from curl import *
from pages.main_page import MainPage



class TestMainPage:
    @allure.title("Пользователь может открыть Конструктор из Ленты заказов")
    def test_user_can_open_constructor_from_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        main_page.click_constructor_button()
        current_page = main_page.is_on_main_page()
        assert Url.MAIN_SITE in current_page

    @allure.title("Пользователь может открыть Конструктор из Личного кабинета")
    def test_user_can_open_constructor_from_profile(self, driver):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        main_page.click_constructor_button()
        current_page = main_page.is_on_main_page()
        assert Url.MAIN_SITE in current_page

    @allure.title("Пользователь может перейти в Конструктор через логотип сайта")
    def test_user_can_open_constructor_by_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        main_page.click_logo()
        current_page = main_page.is_on_main_page()
        assert Url.MAIN_SITE in current_page

    @allure.title("Пользователь может открыть Ленту заказов с главной страницы")
    def test_user_can_open_feed_from_main(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        current_page = main_page.is_on_feed_page()
        assert Url.FEED_PAGE in current_page

    @allure.title("Пользователь может открыть Ленту заказов из Личного кабинета")
    def test_user_can_open_feed_from_profile(self, driver):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        main_page.click_feed_button()
        current_page = main_page.is_on_feed_page()
        assert Url.FEED_PAGE in current_page
