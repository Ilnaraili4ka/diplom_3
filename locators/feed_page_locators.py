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
