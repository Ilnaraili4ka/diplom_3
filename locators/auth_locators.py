from selenium.webdriver.common.by import By


class AuthLocators:
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORM_AUTH = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']")