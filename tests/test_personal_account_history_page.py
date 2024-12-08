import allure
from pages.personal_account_page import PersonalAccountPage
from data.personal_account_page_data import *
from conftest import *
from locators.personal_account_page_locators import *


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Проверка перехода в личный кабинет")
    def test_go_to_personal_account_after_authorization(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page.set_page_zoom(0.7)
        page.go_to_personal_account()
        assert page.find_element(PersonalAccountPageLocators.ORDERS_HISTORY), "Вход не выполнен."

    @allure.title("Проверка перехода в личный кабинет без авторизации")
    def test_go_to_personal_account_without_authorization(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        assert page.find_element(PersonalAccountPageLocators.LOGIN_FORM), "Форма регистрации не найдена"

    @allure.title("Проверка перехода в раздел 'История заказов' с имеющейся историей")
    def test_go_to_orders_history_with_orders_in_it(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page.go_to_personal_account()
        page.go_to_orders_history()
        assert page.find_element(
            PersonalAccountPageLocators.ORDER_INFO), "Элемент с информацией о заказах не найден на странице"

    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page.go_to_personal_account()
        page.logout()
        assert page.find_element(PersonalAccountPageLocators.LOGIN_BUTTON_REGISTRATION_FORM), "Выход не выполнен"
