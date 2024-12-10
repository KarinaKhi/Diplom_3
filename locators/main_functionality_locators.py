from selenium.webdriver.common.by import By


class MainFunctionalityPageLocators:
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    FLUORESCENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    SPIKED_SAUCE = (By.XPATH, "//img[@alt='Соус с шипами Антарианского плоскоходца']")
    BIO_MAGNOLIA_CUTLET = (By.XPATH, "//img[@alt='Биокотлета из марсианской Магнолии']")
    FLUORESCENT_BUN_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    MODAL_WINDOW_ORDER = (By.XPATH, "//*[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    MODAL_WINDOW_INGREDIENT = (By.XPATH, "//*[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']")
    CROSS_BUTTON = (
        By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    ORDER_CONSTRUCTOR = (By.XPATH, "//*[contains(@class, 'BurgerConstructor_basket__listItem__aWMu1')]")
    CREATED_ORDER_NUMBER = (
        By.XPATH,
        "//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    OVERLAYER_FOR_ORDERS = (By.CSS_SELECTOR, "div[class*='Modal_modal__P3_V5']")
