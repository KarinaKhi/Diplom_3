from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    ORDERS_HISTORY = (By.XPATH, '/html/body/div/div/main/div/nav/ul/li[2]/a')
    TEXT_IN_ACCOUNT = (By.XPATH, '//*[@id="root"]/div/main/div/nav/p')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
    ORDER_INFO = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul')
    LOGIN_FORM = (By.XPATH, '//*[@id="root"]/div/main/div/form')
    LOGIN_BUTTON_REGISTRATION_FORM = (By.XPATH, "//button[text()='Войти']")
    EMAIL_INPUT_LOGIN_MAIN_PAGE = (By.XPATH, '//fieldset[1]//input')
    PASSWORD_INPUT_LOGIN_MAIN_PAGE = (By.XPATH, "//fieldset[2]//input")
    LOGIN_LINK_ON_LOGIN_FORM = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    NAME_INPUT = (By.XPATH, "//fieldset[1]//input")
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]//input")
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]//input")
    REGISTER_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/button")
    REGISTER_LINK = (By.XPATH, '/html/body/div/div/main/div/div/p[1]/a')
    LOGIN_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '/html/body/div/div/header/nav/a')
    LAST_ORDER = (By.XPATH, '/html/body/div/div/main/div/div/div/ul/li/a/div[1]/p[1]')
    PERSONAL_ORDER_LIST = (By.XPATH, '/html/body/div/div/main/div/div/div/ul')
    OVERLAYER_FOR_ORDERS = (By.XPATH, '/html/body/div/div/div/div')
    # OVERLAYER_FOR_ORDERS = (By.XPATH, '//*[@id="root"]/div/section/div[2]')
