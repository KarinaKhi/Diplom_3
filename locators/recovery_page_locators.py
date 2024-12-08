from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '/html/body/div/div/header/nav/a/p')
    EMAIL_RECOVERY_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')
    EMAIL_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input')
    RECOVERY_BUTTON_AFTER_EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/div')