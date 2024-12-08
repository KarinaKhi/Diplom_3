from selenium.webdriver.common.by import By


class MainFunctionalityPageLocators:
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    CONSTRUCTOR_BUTTON = (By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a')
    MAIN_PAGE_MAKE_BURGER_TEXT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
    ORDER_FEED = (By.XPATH, '/html/body/div/div/header/nav/ul/li[2]/a')
    ORDER_FEED_PAGE_HEADER = (By.XPATH, '//*[@id="root"]/div/main/div/h1')
    FLUORESCENT_BUN = (By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[1]/a[1]/img')
    SPIKED_SAUCE = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[4]')
    BIO_MAGNOLIA_CUTLET = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[3]')
    CROSS_BUTTON = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/button')
    MODAL_WINDOW_INGREDIENT = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div')
    MODAL_WINDOW = (By.XPATH, "/html/body/div/div/section[1]")
    MODAL_TEXT_INGREDIENT = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div/h2')
    FLUORESCENT_BUN_COUNTER_2 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]')
    SPIKED_SAUCE_COUNTER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[4]/../div/span')
    BIO_MAGNOLIA_CUTLET_COUNTER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[3]/../div/span')
    ORDER_CONSTRUCTOR = (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]')
    MODAL_WINDOW_ORDER = (By.XPATH, '//*[@id="root"]/div/section')
    CLOSED_MODAL_WINDOW = (By.XPATH, '/html/body/div/div/section[1]/div[1]')
    CREATED_ORDER_NUMBER = (By.XPATH, '/html/body/div/div/section/div[1]/div/h2')
    OVERLAYER_FOR_ORDERS = (By.XPATH, '/html/body/div/div/div/div')
