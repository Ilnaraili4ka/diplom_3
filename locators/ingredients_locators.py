from selenium.webdriver.common.by import By


class IngredientsLocators:
    BUN_FLUORESCENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']")
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[.//h2[text()='Детали ингредиента']]//button[contains(@class, 'Modal_modal__close__')]"
    )
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    FLUORESCENT_BUN_COUNTER = (
    By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[contains(@class, 'counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")


