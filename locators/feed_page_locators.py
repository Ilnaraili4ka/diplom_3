from selenium.webdriver.common.by import By

class FeedPageLocators:
    TOTAL_DONE_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    )

    TODAY_DONE_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    )

    ORDERS_IN_PROGRESS_LIST_ITEMS = (
        By.XPATH,
        "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']"
    )
    WINDOW_NUMBER_ORDER= (By.XPATH,
        "//div[@class = 'Modal_modal__contentBox__sCy8X pt-30 pb-30']")

    BUTTON_CLOSE_WINDOW_NUMBER_ORDER = (By.XPATH,
                                        "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")