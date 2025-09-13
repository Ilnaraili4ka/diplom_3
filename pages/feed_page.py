import allure
from selenium.webdriver.common.by import By
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage



class FeedPage(BasePage):

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_done_before_order(self):
        text = self.get_text_on_element(FeedPageLocators.TOTAL_DONE_COUNTER)
        return int(text.replace(" ", "")) if text and text.replace(" ", "").isdigit() else 0

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_done_before_order(self):
        text = self.get_text_on_element(FeedPageLocators.TODAY_DONE_COUNTER)
        return int(text.replace(" ", "")) if text and text.replace(" ", "").isdigit() else 0

    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_orders_in_progress(self):
        return self.get_text_on_element(FeedPageLocators.ORDERS_IN_PROGRESS_LIST_ITEMS)

    @allure.step("Ожидение появления номера заказа")
    def wait_text_number_order(self, order_number):
        self.wait_for_text(FeedPageLocators.ORDERS_IN_PROGRESS_LIST_ITEMS, str(order_number))


    def wait_total_done_counter_increased(self, old_value, timeout=10):

        new_value = self.get_total_done_before_order()
        if new_value > old_value:
            return new_value
        raise AssertionError(f"Счётчик не увеличился за {timeout} секунд. Было: {old_value}")