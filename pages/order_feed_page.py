import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_functionality_locators import MainFunctionalityPageLocators
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def navigate_to_order_feed(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(MainFunctionalityPageLocators.OVERLAYER_FOR_ORDERS)
        )
        self.click_element(OrderFeedPageLocators.ORDER_FEED_SECTION)

    def click_first_order(self):
        self.scroll_into_view(OrderFeedPageLocators.FIRST_ORDER)
        self.click_element(OrderFeedPageLocators.FIRST_ORDER)

    def get_all_orders(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(MainFunctionalityPageLocators.OVERLAYER_FOR_ORDERS)
        )
        counter = self.find_element(OrderFeedPageLocators.ORDERS_LIST)
        raw_text = [line for line in counter.text.split() if len(line) > 0 and line[0] == "#"]
        return raw_text

    def get_orders_in_progress(self, requested_order=None):
        orders_set = set()
        for _ in range(100):
            counter = self.find_element(OrderFeedPageLocators.BOX_WITH_NUMBER_IN_WORK)
            raw_text = [line for line in counter.text.split() if len(line) > 0 and line[0] == "0"]
            orders_set.update(raw_text)
            if requested_order is not None and requested_order in orders_set:
                break
            time.sleep(0.1)
        return orders_set

    def get_counter_value(self, locator):
        element = self.find_element(locator)
        return int(element.text.strip())
