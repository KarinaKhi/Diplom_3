import allure
from data.personal_account_page_data import USER_CREDENTIALS
from locators.main_functionality_locators import MainFunctionalityPageLocators
from pages.main_functionality_page import MainFunctionalityPage
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.personal_account_page import PersonalAccountPage
from conftest import *


@allure.feature("Функциональность Ленты заказов")
class TestOrderFeed:

    @allure.title("Открытие всплывающего окна при клике на заказ")
    def test_order_modal_opens_on_click(self, driver, open_main_page):
        page = OrderFeedPage(driver)
        page.navigate_to_order_feed()
        page.click_first_order()
        assert page.find_element(
            OrderFeedPageLocators.ORDER_DETAILS_MODAL_2), "Модальное окно с деталями заказа не открылось."

    @allure.title("Отображение заказов из 'Истории заказов' в 'Ленте заказов'")
    def test_orders_in_history_appear_in_feed(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page = MainFunctionalityPage(driver)
        page.add_ingredient_to_order(MainFunctionalityPageLocators.FLUORESCENT_BUN)
        page.click_on_order_button()
        created_order_number = page.get_created_orger_number()
        created_order_number_text = f"#0{created_order_number}"
        page.close_modal_window()
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.go_to_orders_history()
        all_personal_orders = page.get_all_orders()
        page = OrderFeedPage(driver)
        page.navigate_to_order_feed()
        all_orders = page.get_all_orders()
        assert created_order_number_text in all_personal_orders and created_order_number_text in all_orders

    @allure.title("Увеличение счётчика 'Выполнено за всё время' при создании нового заказа")
    def test_counter_all_time_increases(self, driver, open_main_page):
        page = OrderFeedPage(driver)
        page.navigate_to_order_feed()
        initial_count = page.get_counter_value(OrderFeedPageLocators.COUNTER_ALL_TIME)
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page = MainFunctionalityPage(driver)
        page.add_ingredient_to_order(MainFunctionalityPageLocators.FLUORESCENT_BUN)
        page.click_on_order_button()
        page.close_modal_window()
        page = OrderFeedPage(driver)
        page.navigate_to_order_feed()
        driver.refresh()
        updated_count = page.get_counter_value(OrderFeedPageLocators.COUNTER_ALL_TIME)
        assert updated_count > initial_count, "'Выполнено за всё время' не увеличилось после создания заказа."

    @allure.title("Увеличение счётчика 'Выполнено за сегодня' при создании нового заказа")
    def test_counter_today_increases(self, driver, open_main_page):
        page = OrderFeedPage(driver)
        page.navigate_to_order_feed()
        initial_count = page.get_counter_value(OrderFeedPageLocators.COUNTER_TODAY)
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page = MainFunctionalityPage(driver)
        page.add_ingredient_to_order(MainFunctionalityPageLocators.FLUORESCENT_BUN)
        page.click_on_order_button()
        page.close_modal_window()
        page = OrderFeedPage(driver)
        page.navigate_to_order_feed()
        updated_count = page.get_counter_value(OrderFeedPageLocators.COUNTER_TODAY)
        assert updated_count > initial_count, "'Выполнено за сегодня' не увеличилось после создания заказа."

    @allure.title("Появление номера заказа в разделе 'В работе' после оформления заказа")
    def test_order_number_appears_in_work_section(self, driver, open_main_page):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account()
        page.enter_user_credentials(USER_CREDENTIALS["email"], USER_CREDENTIALS["password"])
        page.click_enter_button()
        page = MainFunctionalityPage(driver)
        page.add_ingredient_to_order(MainFunctionalityPageLocators.FLUORESCENT_BUN)
        page.click_on_order_button()
        created_order_number = page.get_created_orger_number()
        created_order_number_text = f"0{created_order_number}"
        page.close_modal_window()
        page = OrderFeedPage(driver)
        page.navigate_to_order_feed()
        orders = page.get_orders_in_progress(created_order_number_text)
        assert created_order_number_text in orders
