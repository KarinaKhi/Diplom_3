from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    ORDERS_HISTORY = (By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    LOGIN_LINK_ON_LOGIN_FORM = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    EMAIL_INPUT_LOGIN_MAIN_PAGE = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT_LOGIN_MAIN_PAGE = (By.XPATH, "//input[@name='Пароль']")
    PERSONAL_ORDER_LIST = (By.XPATH, "//*[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']")
    OVERLAYER_FOR_ORDERS = (By.CSS_SELECTOR, "div[class*='Modal_modal__P3_V5']")