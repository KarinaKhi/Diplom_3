from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):

    def go_to_personal_account(self):
        self.wait_for_overlay_to_disappear()
        self.scroll_into_view(PersonalAccountPageLocators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountPageLocators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
        )
        self.click_element(PersonalAccountPageLocators.LOGIN_BUTTON_PERSONAL_ACCOUNT)

    def enter_user_credentials(self, email, password):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountPageLocators.EMAIL_INPUT_LOGIN_MAIN_PAGE)
        )
        email_input.click()
        email_input.send_keys(email)
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountPageLocators.PASSWORD_INPUT_LOGIN_MAIN_PAGE)
        )
        password_input.click()
        password_input.send_keys(password)

    def click_enter_button(self):
        self.click_element(PersonalAccountPageLocators.LOGIN_LINK_ON_LOGIN_FORM)

    def go_to_orders_history(self):
        self.wait_for_overlay_to_disappear()
        self.scroll_into_view(PersonalAccountPageLocators.ORDERS_HISTORY)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(PersonalAccountPageLocators.ORDERS_HISTORY)
        )
        self.click_element(PersonalAccountPageLocators.ORDERS_HISTORY)

    def get_all_orders(self):
        self.scroll_into_view(PersonalAccountPageLocators.PERSONAL_ORDER_LIST)
        counter = self.find_element(PersonalAccountPageLocators.PERSONAL_ORDER_LIST)
        raw_text = [line for line in counter.text.split() if len(line) > 0 and line[0] == "#"]
        return raw_text

    def logout(self):
        self.wait_for_overlay_to_disappear()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountPageLocators.LOGOUT_BUTTON)
        )
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON)
        )
        element.click()

    def wait_for_overlay_to_disappear(self):
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(PersonalAccountPageLocators.OVERLAYER_FOR_ORDERS)
        )
