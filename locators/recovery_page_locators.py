from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    EMAIL_RECOVERY_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")
    RECOVERY_BUTTON_AFTER_EMAIL_INPUT = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    EMAIL_FIELD = (By.XPATH, "//input[@type='text' and @name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
