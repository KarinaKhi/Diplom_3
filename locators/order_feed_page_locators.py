from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_SECTION = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDERS_LIST = (By.XPATH, "//*[@class='OrderFeed_list__OLh59']")
    COUNTER_ALL_TIME = (
        By.XPATH, "//div[.//p[text()='Выполнено за все время:']]//p[contains(@class, 'OrderFeed_number')]")
    COUNTER_TODAY = (
        By.XPATH, "//div[.//p[contains(text(), 'Выполнено за сегодня:')]]//p[contains(@class, 'OrderFeed_number')]")
    BOX_WITH_NUMBER_IN_WORK = (By.XPATH, "//*[contains(@class, 'OrderFeed_orderListReady')]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//*[contains(@class, 'Modal_orderBox__1xWdi')]")
    FIRST_ORDER = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')]//a)[1]")