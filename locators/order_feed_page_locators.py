from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_SECTION = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[2]/a/p')
    ORDERS_LIST = (By.XPATH, '/html/body/div/div/main/div/div/ul')
    FIRST_ORDER = (By.XPATH, '/html/body/div/div/main/div/div/ul/li[1]/a')
    ORDER_DETAILS_MODAL_2 = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]')
    BOX_WITH_NUMBER_IN_WORK = (By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/ul[2]')
    COUNTER_ALL_TIME = (
        By.XPATH, "/html/body/div/div/main/div/div/div/div[2]/p[2]")
    COUNTER_TODAY = (
        By.XPATH, "/html/body/div/div/main/div/div/div/div[3]/p[2]")
    CROSS_BUTTON = (By.XPATH, '/html/body/div/div/section[2]/div[1]/button')
