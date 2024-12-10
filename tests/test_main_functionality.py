from conftest import *
import allure
from data.personal_account_page_data import USER_CREDENTIALS
from pages.main_functionality_page import MainFunctionalityPage
from locators.main_functionality_locators import MainFunctionalityPageLocators
from pages.personal_account_page import PersonalAccountPage


@allure.feature("Тестирование основного функционала")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigation_to_constructor_without_authorization(self, driver, open_main_page):
        page = MainFunctionalityPage(driver)
        page.click_on_constructor_button()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(BASE_URL)
        assert BASE_URL in driver.current_url, "Не удалось перейти на страницу конструктора"

    @allure.title("Переход на «Конструктор» после авторизации")
    def test_navigation_to_constructor_after_authorization(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page = MainFunctionalityPage(driver)
        page.click_on_constructor_button()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(BASE_URL)
        assert BASE_URL in driver.current_url, "Не удалось перейти на страницу конструктора"

    @allure.title("Переход по клику на «Конструктор» из личного кабинета")
    def test_navigation_to_constructor_from_personal_account(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page.go_to_personal_account()
        page = MainFunctionalityPage(driver)
        page.click_on_constructor_button()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(BASE_URL)
        assert BASE_URL in driver.current_url, "Не удалось перейти на страницу конструктора"

    @allure.title("Переход по клику на «Лента заказов» из личного кабинета")
    def test_navigation_to_order_feed_from_personal_account(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page.go_to_personal_account()
        page = MainFunctionalityPage(driver)
        page.click_on_order_feed_button()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(FEED_URL)
        assert FEED_URL in driver.current_url, "Не удалось перейти на страницу ленты заказов"

    @allure.title("Переход по клику на «Лента заказов» с главной страницы после авторизации")
    def test_navigation_to_order_feed_from_main_page_after_authorization(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page = MainFunctionalityPage(driver)
        page.click_on_order_feed_button()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(FEED_URL)
        assert FEED_URL in driver.current_url, "Не удалось перейти на страницу ленты заказов"

    @allure.title("Переход по клику на «Лента заказов» с главной страницы")
    def test_navigation_to_order_feed(self, driver, open_main_page):
        page = MainFunctionalityPage(driver)
        page.click_on_order_feed_button()
        driver.switch_to.window(driver.window_handles[-1])
        page.wait_for_url_upd(FEED_URL)
        assert FEED_URL in driver.current_url, "Не удалось перейти на страницу ленты заказов"

    @allure.title("Открытие всплывающего окна при клике на ингредиент")
    def test_modal_window_opens_on_click(self, driver, open_main_page):
        page = MainFunctionalityPage(driver)
        page.click_on_ingredient(MainFunctionalityPageLocators.FLUORESCENT_BUN)
        assert page.find_element(
            MainFunctionalityPageLocators.MODAL_WINDOW_INGREDIENT),\
            "Модальное окно с деталями ингредиента не открылось."

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_modal_window_closes_on_cross_click(self, driver, open_main_page):
        page = MainFunctionalityPage(driver)
        page.click_on_ingredient(MainFunctionalityPageLocators.FLUORESCENT_BUN)
        page.close_modal_window()
        assert page.is_modal_window_closed(), "Модальное окно не закрылось."

    @allure.title("Увеличение счетчика ингредиента при добавлении в заказ")
    def test_add_ingredient_increases_counter(self, driver, open_main_page):
        page = MainFunctionalityPage(driver)
        page.add_ingredient_to_order(MainFunctionalityPageLocators.FLUORESCENT_BUN)
        assert page.is_ingredient_counter_updated(MainFunctionalityPageLocators.FLUORESCENT_BUN_COUNTER), \
            "Счетчик для ингредиента не увеличился после добавления в заказ."

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page = MainFunctionalityPage(driver)
        page.add_ingredient_to_order(MainFunctionalityPageLocators.FLUORESCENT_BUN)
        page.add_ingredient_to_order(MainFunctionalityPageLocators.SPIKED_SAUCE)
        page.click_on_order_button()
        assert page.find_element(
            MainFunctionalityPageLocators.MODAL_WINDOW_ORDER), \
            "Не удалось оформить заказ для авторизованного пользователя."

    @allure.title("Авторизованный пользователь видит кнопку оформить заказ")
    def test_logged_in_user_can_see_order_button(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page = MainFunctionalityPage(driver)
        assert page.find_element(
            MainFunctionalityPageLocators.ORDER_BUTTON), \
            "Не удалось найти кнопку заказа для авторизованного пользователя."
