from selenium.webdriver.common.by import By



class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'text_type_digits-large')]"
    )
    BUTTON_CLOSE_WINDOW_NUMBER_ORDER = (By.XPATH,
                                        "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    WINDOW_NUMBER_ORDER= (By.XPATH,
        "//div[@class = 'Modal_modal__contentBox__sCy8X pt-30 pb-30']")
