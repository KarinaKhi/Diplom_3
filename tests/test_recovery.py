import allure
from pages.recovery_page import RecoveryPage
from conftest import *
from locators.recovery_page_locators import *


@allure.feature("Password Recovery")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_recovery_button_redirects_to_recovery_page(self, driver, open_main_page):
        page = RecoveryPage(driver)
        page.click_login_button_personal_account()
        page.click_email_recovery_button()
        assert driver.find_element(
            *RecoveryPageLocators.RECOVERY_BUTTON_AFTER_EMAIL_INPUT).is_displayed(), \
            "Страница восстановления пароля не открылась"
        page.click_recovery_button_after_email_input()

    @allure.title("Ввод почты и клик по кнопке восстановления")
    def test_enter_email_and_submit(self, driver, open_main_page):
        page = RecoveryPage(driver)
        page.click_login_button_personal_account()
        page.click_email_recovery_button()
        page.enter_email("test@example.com")
        page.click_recovery_button_after_email_input()
        assert "Восстановление пароля" in driver.page_source, "Сообщение о восстановлении пароля отсутствует"

    @allure.title("Показать/Скрыть пароль делает поле активным")
    def test_show_password_activates_field(self, driver, open_main_page):
        page = RecoveryPage(driver)
        page.click_login_button_personal_account()
        page.click_email_recovery_button()
        page.enter_email("test@example.com")
        page.click_recovery_button_after_email_input()
        page.click_show_password()
        assert page.is_password_field_active(), "Поле ввода пароля не стало активным после нажатия 'Показать пароль'"


