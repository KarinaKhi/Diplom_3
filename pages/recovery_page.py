from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators


class RecoveryPage(BasePage):
    def click_login_button_personal_account(self):
        self.wait_driver.until(
            EC.element_to_be_clickable(RecoveryPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        self.click_element(RecoveryPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_email_recovery_button(self):
        self.scroll_to_element(RecoveryPageLocators.EMAIL_RECOVERY_BUTTON)
        self.click_element(RecoveryPageLocators.EMAIL_RECOVERY_BUTTON)

    def enter_email(self, email):
        email_field = self.driver.find_element(*RecoveryPageLocators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

    def click_recovery_button_after_email_input(self):
        self.driver.find_element(*RecoveryPageLocators.RECOVERY_BUTTON_AFTER_EMAIL_INPUT).click()

    def click_show_password(self):
        self.wait_driver.until(
            EC.element_to_be_clickable(RecoveryPageLocators.SHOW_PASSWORD_BUTTON)
        )
        self.click_element(RecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):
        password_field = self.wait_for_element_to_be_visible(RecoveryPageLocators.PASSWORD_FIELD)
        return password_field.is_displayed()
