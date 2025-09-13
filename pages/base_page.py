import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Дождаться видимости окна')
    def wait_for_visible_and_interactable(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return element

    @allure.step('Проверка присутствия элемента')
    def check_presence(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание определенного текста в элементе')
    def wait_for_text(self, locator, expected_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        EC.text_to_be_present_in_element(locator, expected_text)
    )
    @allure.step('Открыть указанный URL')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Возвращает текущий URL')
    def current_url(self):
        return self.driver.current_url