from data import DataIngredients
from pages.auth_page import AuthPage
from pages.ingredients import Ingredients
from pages.main_page import MainPage
from pages.feed_page import *
import allure
from pages.request_metods import RequestMetods


class TestOrderFeed:

    @allure.title("Счётчик 'Выполнено за все время' увеличивается после создания заказа")
    def test_done_allday_counter_increases(self, authorized_user):
        driver = authorized_user["driver"]
        main_page = MainPage(driver)
        feed_page= FeedPage(driver)
        ingredients = Ingredients(driver)
        auth= AuthPage(driver)

        with allure.step("Авторизация"):
            password=authorized_user["password"]
            email=authorized_user["email"]
            main_page.click_profile_button()
            auth.auth(password, email)
        with allure.step("1. Получить исходное значение счётчика 'Выполнено за все время'"):
            main_page.click_feed_button()
            before = feed_page.get_total_done_before_order()
        with (allure.step('2. Создать заказ через UI')):
            main_page.open_main_page()
            source = ingredients.get_fluorescent_bun_element()
            target = ingredients.get_constructor_area()
            ingredients.drag_and_drop_element(source, target)
            ingredients.click_button_order()
            main_page.main_page_loading_wait()
            feed_page.window_number_order_is_open()
            feed_page.wait_window_number_order()
            main_page.main_page_loading_wait()
            feed_page.click_close_window_number_order()
        with allure.step("3. Проверить увеличение счётчика 'Выполнено за все время'"):
            main_page.click_feed_button()
            after = feed_page.get_total_done_before_order()
            assert after > before, f"Счётчик не увеличился: было {before}, стало {after}"


    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_done_today_counter_increases(self, authorized_user):
        driver = authorized_user["driver"]
        main_page = MainPage(driver)
        feed_page= FeedPage(driver)
        ingredients = Ingredients(driver)
        auth= AuthPage(driver)

        with allure.step("Авторизация"):
            password=authorized_user["password"]
            email=authorized_user["email"]
            main_page.click_profile_button()
            auth.auth(password, email)
        with allure.step("1. Получить исходное значение счётчика 'Выполнено за сегодня'"):
            main_page.click_feed_button()
            before = feed_page.get_today_done_before_order()
        with (allure.step('2. Создать заказ через UI')):
            main_page.open_main_page()
            source = ingredients.get_fluorescent_bun_element()
            target = ingredients.get_constructor_area()
            ingredients.drag_and_drop_element(source, target)
            ingredients.click_button_order()
            main_page.main_page_loading_wait()
            feed_page.window_number_order_is_open()
            feed_page.wait_window_number_order()
            main_page.main_page_loading_wait()
            feed_page.click_close_window_number_order()
        with allure.step("3. Проверить увеличение счётчика 'Выполнено за сегодня'"):
            main_page.click_feed_button()
            after = feed_page.get_today_done_before_order()
            assert after > before, f"Счётчик не увеличился: было {before}, стало {after}"


    @allure.title("Номер нового заказа отображается в разделе 'В работе'")
    def test_number_appears_in_progress(self, authorized_user):
        driver = authorized_user["driver"]
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        with allure.step("1. Открыть страницу Лента заказов"):
            main_page.click_feed_button()
        with allure.step('2. Создать заказ через API и получить его номер'):
            access_token = authorized_user["access_token"]
            headers = {"Authorization": access_token}
            data = {"ingredients": DataIngredients.data_ingredients}
            create_order= RequestMetods.create_order(headers=headers, data=data)
            order_number=create_order.json()["order"]["number"]
        with allure.step("3. Проверить наличие номера заказа в разделе 'В работе'"):
            feed_page.wait_text_number_order(order_number)
            order_in_progress = feed_page.get_orders_in_progress()
            assert str(order_number) in order_in_progress, f"Заказ {order_number} не найден в разделе 'В работе'"
