import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.ingredients_locators import IngredientsLocators

class Ingredients(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Кликнуть на ингредиент Флюоресцентная булка R2-D3")
    def click_bun_ingredient(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.click_on_element(IngredientsLocators.BUN_FLUORESCENT)

    @allure.step("Проверить, что модальное окно отображается")
    def is_modal_visible(self):
        return self.wait_for_element(IngredientsLocators.MODAL_WINDOW)

    @allure.step("Проверить наличие заголовка 'Детали ингредиента'")
    def is_modal_title_correct(self):
        title = self.get_text_on_element(IngredientsLocators.MODAL_TITLE)
        return title == "Детали ингредиента"

    @allure.step("Кликнуть на кнопку закрытия модального окна")
    def click_close_modal(self):
        self.click_on_element(IngredientsLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        self.wait_for_element_hide(IngredientsLocators.MODAL_WINDOW)
        return True

    @allure.step("Получить текущее значение счётчика ингредиента")
    def get_fluorescent_bun_counter(self):
        text = self.get_text_on_element(IngredientsLocators.FLUORESCENT_BUN_COUNTER)
        return int(text) if text.isdigit() else 0

    @allure.step("Получить элемент ингредиента 'Флюоресцентная булка'")
    def get_fluorescent_bun_element(self):
        return self.wait_for_element(IngredientsLocators.BUN_FLUORESCENT)

    @allure.step("Получить элемент зоны конструктора")
    def get_constructor_area(self):
        return self.wait_for_element(IngredientsLocators.CONSTRUCTOR_AREA)






