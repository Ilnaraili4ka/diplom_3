import allure
from pages.ingredients import Ingredients


class TestIngredients:
    @allure.title("Пользователь может открыть модальное окно ингредиента")
    def test_user_can_open_ingredient_modal(self, driver):
        ingredients = Ingredients(driver)
        with allure.step("Пользователь кликает по ингредиенту"):
            ingredients.click_bun_ingredient()

        with allure.step("Проверка появления модального окна"):
            assert ingredients.is_modal_visible()

        with allure.step("Проверка корректности заголовка модального окна"):
            assert ingredients.is_modal_title_correct()

    @allure.title("Пользователь может закрыть модальное окно ингредиента")
    def test_user_can_close_ingredient_modal_on_cross(self, driver):
        ingredients = Ingredients(driver)
        with allure.step("Пользователь кликает по ингредиенту"):
            ingredients.click_bun_ingredient()

        with allure.step("Убедиться, что модальное окно открылось"):
            assert ingredients.is_modal_visible()

        with allure.step("Пользователь закрывает модальное окно по крестику"):
            ingredients.click_close_modal()

        with allure.step("Проверка, что модальное окно закрыто"):
            assert ingredients.is_modal_closed()

    @allure.title("Счётчик ингредиента увеличивается после добавления в заказ")
    def test_ingredient_counter_increases_after_drag_and_drop(self, driver):
        ingredients = Ingredients(driver)
        with allure.step("Получаем текущее значение счётчика ингредиента"):
            initial_count = ingredients.get_fluorescent_bun_counter()

        source = ingredients.get_fluorescent_bun_element()
        target = ingredients.get_constructor_area()

        with allure.step("Пользователь перетаскивает ингредиент в конструктор"):
            ingredients.drag_and_drop_element(source, target)

        with allure.step("Проверяем, что счётчик ингредиента увеличился"):
            new_count = ingredients.get_fluorescent_bun_counter()
            assert new_count == initial_count + 2
