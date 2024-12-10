import allure
from pages.personal_account_page import PersonalAccountPage
from data.personal_account_page_data import *
from conftest import *


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Проверка перехода в личный кабинет после авторизации пользователя")
    def test_go_to_personal_account_after_authorization(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page.go_to_personal_account()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(ACCOUNT_PROFILE_URL)
        assert ACCOUNT_PROFILE_URL in driver.current_url, \
            "Не удалось перейти на страницу персонального аккаунта пользователя"

    @allure.title("Проверка перехода в личный кабинет без авторизации")
    def test_go_to_personal_account_without_authorization(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(LOGIN_FORM_URL)
        assert LOGIN_FORM_URL in driver.current_url, \
            "Не удалось перейти на страницу формы авторизации"

    @allure.title("Проверка перехода в раздел 'История заказов' на изменение URL")
    def test_go_to_orders_history_url_change(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page.go_to_personal_account()
        page.go_to_orders_history()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(HISTORY_URL)
        assert HISTORY_URL in driver.current_url, "Не удалось перейти на страницу Истории"

    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page.go_to_personal_account()
        page.logout()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(LOGIN_FORM_URL)
        assert LOGIN_FORM_URL in driver.current_url, "Не удалось перейти на страницу формы авторизации"
